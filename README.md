# ai_sop_toolkit

A lightweight Python CLI toolkit that bootstraps an AI Agent Team development SOP into any new project directory.

## 中文說明

`ai_sop_toolkit` 是一個輕量的 Python CLI 工具，目的是在任何新專案資料夾中，快速建立一套 AI Agent Team 協作開發 SOP。

安裝完成後，只要在目標專案資料夾執行：

```bash
ai-sop init
```

工具就會自動建立以下檔案：

- `.cursorrules`
- `CLAUDE.md`
- `TASK.md`
- `PROJECT_RULES.md`
- `AGENTS.md`

這些檔案可用來統一 AI 協作時的需求釐清、任務拆解、驗證流程、代理人職位切換與開發規範。

### V1.3 新增重點

- 新增 `AGENTS.md`，定義 PM、Architect、Builder、Tester、Liaison 五種角色
- 讓 AI 能根據 `TASK.md` 階段切換對應職位
- 在每次完成任務後，透過 Liaison 模式做摘要與交棒

### 適合的使用情境

- 想替每個新專案快速注入固定的 AI 開發流程
- 想讓 Cursor、Claude Code 或其他 AI 助手遵守一致的 SOP
- 想把團隊開發規範模板化、可重複使用

### 安裝方式

在專案根目錄執行：

```bash
pip install -e .
```

若你的環境使用 Windows 啟動器，也可以使用：

```bash
py -m pip install -e .
```

### 使用方式

進入任一新專案資料夾後執行：

```bash
ai-sop init
```

如果目標檔案已存在，CLI 會詢問你是否要覆蓋。

### 建議操作流程

1. 在本機安裝這個工具。
2. 到新的空白專案資料夾執行 `ai-sop init`。
3. 打開 Cursor、Claude Code 或其他 AI 工具。
4. 請 AI 先閱讀 `PROJECT_RULES.md`、`TASK.md` 與其他規範檔。
5. 依照 SOP 進行需求釐清、開發與驗證。

## English Overview

After installation, run `ai-sop init` inside a target project folder to generate:

- `.cursorrules`
- `CLAUDE.md`
- `TASK.md`
- `PROJECT_RULES.md`
- `AGENTS.md`

These files help standardize requirement discovery, task tracking, validation, agent role switching, and development guardrails for AI-assisted coding workflows.

## Project Structure

```text
ai_sop_toolkit/
├── setup.py
├── README.md
└── ai_sop_toolkit/
    ├── __init__.py
    ├── cli.py
    └── templates/
        ├── cursorrules.tpl
        ├── claude_md.tpl
        ├── task_md.tpl
        └── project_rules_tpl.md
```

## Installation

From the project root:

```bash
pip install -e .
```

Using editable mode means you can update template files without reinstalling the package.

If you want to install it as a normal package later:

```bash
pip install .
```

## Usage

Move into any new or existing project folder and run:

```bash
ai-sop init
```

The CLI will copy the built-in templates into the current working directory. If a target file already exists, the tool will ask whether it should be overwritten.

## Generated Files

- `.cursorrules`: Core SOP instructions for AI coding assistants.
- `CLAUDE.md`: Project rules and prohibitions.
- `TASK.md`: Task progress tracking template.
- `PROJECT_RULES.md`: Project alignment template for goals, scope, and constraints.
- `AGENTS.md`: Agent Team role definitions and handover protocol.

## Local Testing

Run the test suite from the project root:

```bash
python -m pytest
```

Or with the Windows launcher:

```bash
py -m pytest
```

## Publish To GitHub

Push this folder to the configured GitHub repository:

```bash
git add .
git commit -m "Update ai_sop_toolkit"
git push
```

If you move this project to a different repository later, update the URLs in `setup.py` and `pyproject.toml`.

## Development Notes

- Package name: `ai_sop_toolkit` (V1.3)
- CLI command: `ai-sop`
- Main CLI implementation: `ai_sop_toolkit/cli.py`
- Template assets live in: `ai_sop_toolkit/templates/`

## Roadmap Ideas

- Add customizable template profiles.
- Support non-interactive overwrite flags such as `--force`.
- Publish to PyPI after final package validation.

## License

MIT
