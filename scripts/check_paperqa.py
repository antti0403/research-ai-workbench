"""Check PaperQA PDF ingestion and source contexts without model or network calls."""
import asyncio
import json
import os
from pathlib import Path
import socket
import tempfile
from unittest.mock import patch


class NoModels:
    async def call_single(self, *args, **kwargs):
        raise AssertionError('A model was called during the local smoke check')

    async def embed_documents(self, *args, **kwargs):
        raise AssertionError('An embedding model was called during the local smoke check')


def check():
    original_connect = socket.socket.connect

    def local_connect(sock, address):
        # Windows asyncio may use a loopback socket for its event-loop wakeup.
        if not isinstance(address, tuple) or address[0] not in ('127.0.0.1', '::1'):
            raise AssertionError('Outbound network access during the local smoke check')
        return original_connect(sock, address)

    with tempfile.TemporaryDirectory(prefix='paperqa-check-') as temporary, patch.dict(
        os.environ, {'PQA_HOME': temporary, 'LITELLM_LOCAL_MODEL_COST_MAP': 'True'}
    ), patch.object(socket.socket, 'connect', local_connect):
        from paperqa import Docs, Settings
        from paperqa.types import PQASession
        from pypdf import PdfWriter
        from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject

        pdf = Path(temporary) / 'synthetic.pdf'
        writer = PdfWriter()
        page = writer.add_blank_page(width=300, height=200)
        font = DictionaryObject({NameObject('/Type'): NameObject('/Font'), NameObject('/Subtype'): NameObject('/Type1'), NameObject('/BaseFont'): NameObject('/Helvetica')})
        page[NameObject('/Resources')] = DictionaryObject({NameObject('/Font'): DictionaryObject({NameObject('/F1'): writer._add_object(font)})})
        stream = DecodedStreamObject()
        stream.set_data(b'BT /F1 12 Tf 20 100 Td (Synthetic check: sample power is 10 watts.) Tj ET')
        page[NameObject('/Contents')] = writer._add_object(stream)
        writer.write(pdf)
        settings = Settings(
            parsing={'use_doc_details': False, 'multimodal': False, 'defer_embedding': True},
            answer={'evidence_retrieval': False, 'evidence_skip_summary': True},
        )

        async def ingest():
            docs = Docs()
            added = await docs.aadd(pdf, citation='Workbench synthetic fixture, 2026.', docname='Fixture2026', settings=settings, llm_model=NoModels())
            assert added and len(docs.docs) == 1
            assert any('10 watts' in text.text for text in docs.texts)
            assert await docs.aadd(pdf, citation='Workbench synthetic fixture, 2026.', docname='Fixture2026', settings=settings, llm_model=NoModels()) is None
            session = await docs.aget_evidence('What is the sample power?', settings=settings, embedding_model=NoModels(), summary_llm_model=NoModels())
            restored = PQASession.model_validate_json(session.model_dump_json())
            assert restored.contexts and not restored.answer
            context = restored.contexts[0]
            assert '10 watts' in context.context
            assert context.text.doc.citation == 'Workbench synthetic fixture, 2026.'
            assert context.text.name == 'Fixture2026 pages 1-1'
            assert context.text.doc.content_hash
            output = Path(temporary) / 'evidence.json'
            output.write_text(restored.model_dump_json(), encoding='utf-8')
            assert json.loads(output.read_text(encoding='utf-8'))['contexts']

        asyncio.run(ingest())
    print('PaperQA: synthetic PDF, duplicate ingestion, page-linked evidence, and JSON round trip passed; model answering not tested.')


if __name__ == '__main__':
    check()
