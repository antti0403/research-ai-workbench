[English](README.md) | [简体中文](README.zh-CN.md)

# Research AI Workbench

一个本地科研 AI 工作区脚手架。包含自动化安装脚本与面向 Coding Agent 的单文件配置规范，先搭建轻量基础底座，再由 AI 助手根据具体研究课题按需安装专业工具。

[![Installer checks](https://github.com/antti0403/research-ai-workbench/actions/workflows/ci.yml/badge.svg)](https://github.com/antti0403/research-ai-workbench/actions/workflows/ci.yml)

---

## 为什么做这个

用 AI 辅助学术科研通常会遇到两个极端：
1. **白板问题**：在空目录里直接和模型对话。模型没有本地文献检索工具，没有放阅读笔记的地方，读 PDF 容易出现幻觉，也没有规范的科研严谨性约束。
2. **环境臃肿**：很多项目一上来就安装几十个庞大的第三方库，耗费大量磁盘空间，还容易引发本地 Python 依赖冲突。

这个项目采用“渐进式配置”的思路：
- **先搭核心骨架**：初始化一个干净的工作区目录（默认位于 `~/ResearchWorkbench`），配置独立的 PDF 解析与文献提取运行环境，并写入持久化的科研提示词与受控语言规约。
- **Agent 按需补充**：在常用的编程助手（Codex、Claude Code、Cursor 等）中打开该目录。Agent 会主动询问你当前的研究方向与具体课题，只安装当前任务真正需要的扩展工具。

---

## 核心构成

- **科研工作区结构**：预设清晰的目录分层，规范收纳原始文献、阅读笔记、中间数据与论文草稿。
- **独立 PDF 解析环境**：提供隔离的 Python 运行环境用于论文解析与文本提取，不污染全局环境。
- **持久化科研准则**：内置关于证据等级、公式推导完整性、避免无根据推断的交互规范。参考了 ASD-STE100 航空标准与 Karpathy 的输出阶梯理念。
- **可选学科扩展**：根据实际需要接入工具，包括 arXiv / Semantic Scholar 文献检索、PaperQA 循证问答、SymPy 符号推导、单位换算校验、MATLAB 联动指导与科研绘图等。

---

## 快速上手

克隆仓库到本地：

```bash
git clone https://github.com/antti0403/research-ai-workbench.git
cd research-ai-workbench
```

根据你的操作系统运行安装脚本：

**macOS / Linux:**
```bash
bash install.sh
```

**Windows (PowerShell):**
```powershell
.\install.ps1
```

默认工作区路径为 `~/ResearchWorkbench`。如果希望放在其他路径，可以传入参数 `--workspace "path/to/project"`。

脚本安装完成后，在你的 AI Agent 中打开该工作区目录，发送以下提示词：

> 请阅读 START_HERE.md 并为我定制科研工作台。只针对缺失的关键任务细节向我提问，优先复用现有工具，在我的授权范围内按需安装扩展，并验证一个小任务。使用我偏好的语言交流。

如果你希望跳过安装脚本、直接让 AI Agent 全程自主搭建工作区，只需把仓库里的 `SETUP.md` 发给它即可，该文件设计为完全独立可用。

---

## 本地检查与体检命令

仓库附带了 `workbench.py` 工具，用于检查与维护工作区状态：

```bash
# 预览计划安装的组件与环境状态
python workbench.py plan

# 对现有工作区环境进行体检
python workbench.py doctor --workspace "path/to/project"
```

安装过程仅下载公开的开源依赖，不上传任何本地科研文件，也不强制要求额外的付费模型订阅。

---

## 完整文档索引

- [SETUP.md](SETUP.md)：面向 AI Agent 的单文件完整配置指南。
- [SKILLS.md](SKILLS.md)：已验证的科研技能与可选候选清单。
- [docs/FIRST_TASK.md](docs/FIRST_TASK.md)：从零开始完成第一个科研任务的上手演练。
- [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md)：系统平台、Python 版本要求与兼容性边界。
- [docs/AUTOMATION.md](docs/AUTOMATION.md)：自动化参数配置与 CLI 参考。

---

## 鸣谢与开源协议

本项目原创代码与文档遵循 [MIT License](LICENSE)。

致谢：
- 技能原型与实现参考自 **袁一哲 / Yuan1z0825 (Nature Skills)** 与 **K-Dense Inc. (Scientific Agent Skills)**。
- 渐进式工作流设计灵感来自 **艺雨YiLight**，并参考了 **sunweihunu** 整理的实践记录。
- 交互与受控输出准则借鉴了 **ASD-STE100** 标准与 **Andrej Karpathy** 的技术表达建议。
- 外部集成组件保留各自原始协议，详见 [NOTICE.md](NOTICE.md) 与 [THIRD_PARTY.md](THIRD_PARTY.md)。
