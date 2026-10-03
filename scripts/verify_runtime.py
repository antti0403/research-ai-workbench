"""Run small, deterministic checks; these are not scientific validation."""
import importlib.metadata
import io
import json
import os
from pathlib import Path
import sys
import tempfile

profile, requirements = sys.argv[1:]
for requirement in json.loads(requirements):
    name, version = requirement.split('==')
    if importlib.metadata.version(name) != version:
        raise RuntimeError('Version mismatch: ' + name)
if profile == 'core':
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject
    writer = PdfWriter()
    page = writer.add_blank_page(width=300, height=200)
    font = DictionaryObject({NameObject('/Type'): NameObject('/Font'), NameObject('/Subtype'): NameObject('/Type1'), NameObject('/BaseFont'): NameObject('/Helvetica')})
    page[NameObject('/Resources')] = DictionaryObject({NameObject('/Font'): DictionaryObject({NameObject('/F1'): writer._add_object(font)})})
    stream = DecodedStreamObject()
    stream.set_data(b'BT /F1 12 Tf 30 100 Td (Workbench source check) Tj ET')
    page[NameObject('/Contents')] = writer._add_object(stream)
    buffer = io.BytesIO()
    writer.write(buffer)
    buffer.seek(0)
    assert 'Workbench source check' in PdfReader(buffer).pages[0].extract_text()
    print('PDF round trip: generated text extracted correctly.')
elif profile == 'symbolic':
    import sympy as s
    x = s.symbols('x', real=True)
    assert s.diff(s.sin(x)**2 + s.cos(x)**2, x) == 0
    assert s.solve(s.Eq(x**2, 4), x) == [-2, 2]
    print('Symbolic derivative and equation checks passed.')
elif profile == 'units':
    import pint
    from uncertainties import ufloat
    u = pint.UnitRegistry()
    assert (2 * u.ampere * 5 * u.volt).to(u.watt).magnitude == 10
    try:
        (1 * u.meter).to(u.second)
    except pint.DimensionalityError:
        pass
    else:
        raise AssertionError('Incompatible units were accepted.')
    assert abs((ufloat(2, .1) * 3).std_dev - .3) < 1e-12
    print('Power units, incompatible units, and uncertainty checks passed.')
elif profile == 'paperqa':
    from check_paperqa import check
    check()
elif profile in ('data', 'figures'):
    with tempfile.TemporaryDirectory() as temporary:
        os.environ['MPLCONFIGDIR'] = temporary
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import numpy as np
        assert np.isclose(np.mean([1, 2, 3]), 2)
        if profile == 'data':
            import pandas as pd
            from scipy import stats
            assert pd.DataFrame({'x': [1, 2, 3]})['x'].sum() == 6
            assert np.isclose(stats.norm.cdf(0), .5)
        figure, axis = plt.subplots()
        axis.plot([0, 1], [0, 1])
        output = Path(temporary) / 'check.png'
        figure.savefig(output)
        plt.close(figure)
        assert output.read_bytes().startswith(b'\x89PNG')
    print('Small numerical and exported-figure checks passed.')
else:
    raise ValueError('No runtime check defined for ' + profile)
