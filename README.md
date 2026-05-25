# ai_agent_sop_toolkit

[![CI](https://github.com/perry121108-dotcom/ai_agent_sop_toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/perry121108-dotcom/ai_agent_sop_toolkit/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> **2026 現代多代理人協作自動化流程工具箱。**
> 一行指令，在任何專案內植入一套「**證據驅動、角色物理隔離**」的 AI 開發 SOP；讓 PM、架構師、開發、測試、協調官五個代理人各司其職，並以**機器可驗證的證據**作為任務完成的唯一標準。

```bash
pip install -e .
ai-sop init
```

---

## 這是什麼

`ai_agent_sop_toolkit` 是一個可用 pip 安裝的 Python CLI。在任意專案資料夾執行 `ai-sop init`，即可在 5 秒內植入一整套 AI 代理人協作規範檔。

它要根除多代理（Claude Code / Cursor / Gemini 等）協作開發時最常見的兩個失效模式：

1. **文件劇場**：AI 宣稱「測試通過」，卻拿不出任何實際執行證據。
2. **球員兼裁判**：同一個對話 Session 既寫程式又「自我驗收」，盲點互相掩蓋。

本工具箱以兩條鐵律從制度上根除這兩個問題（見下方核心機制）。

---

## 快速開始

```bash
# 安裝
git clone https://github.com/perry121108-dotcom/ai_agent_sop_toolkit
cd ai_agent_sop_toolkit
pip install -e .

# 驗證
ai-sop --version      # ai-sop, version 1.3.0

# 在任意專案內植入協作 SOP
cd /path/to/your-project
ai-sop init
```

> 若目標檔案已存在，CLI 會逐一詢問是否覆蓋，**不會靜默刪除任何內容**。

執行結果：

```text
🚀 正在注入 Agent Team 開發小隊技能 (V1.3)...
✅ 已建立 .cursorrules
✅ 已建立 CLAUDE.md
✅ 已建立 TASK.md
✅ 已建立 WORKLOG.md
✅ 已建立 PROJECT_RULES.md
✅ 已建立 AGENTS.md
🎉 初始化成功！
```

---

## 產生的協作檔案

| 檔案 | 定位 | 用途 |
|------|------|------|
| `.cursorrules` | Orchestrator 主控台 | 依 `TASK.md` 階段切換角色、Session 斷點、證據協議 |
| `CLAUDE.md` | 專案鐵律 | 規範與禁止事項（含證據鐵律、隔離鐵律） |
| `AGENTS.md` | 職位說明書 | 五角色的職責、邊界與交接協議 |
| `TASK.md` | 任務狀態機 | `[ ] → [/] → [x]`；AC 須為可執行指令／自動化斷言 |
| `WORKLOG.md` | 證據帳本 | 測試指令／預期結果／實際執行證據 ＋ `<Execution_Evidence>` 區塊 |
| `PROJECT_RULES.md` | 共識文件 | 目標、範圍與技術限制 |

---

## 五角色 Agent Team

AI 依 `TASK.md` 目前階段，自動扮演最適合的角色：

| 角色 | 負責階段 | 核心職責 |
|------|---------|---------|
| **[PM] 專案經理** | Phase 1 / 5 | 釐清需求、定義**可執行的 AC**、界定 Out of Scope |
| **[Architect] 系統架構師** | Phase 2 | 定義 Schema、核心介面與技術棧，寫入 `PROJECT_RULES.md` |
| **[Builder] 程式開發員** | Phase 3 | 寫業務邏輯**並產出對應自動化測試**，完成後生成交接檔 |
| **[Tester] CI/CD 執行官** | Phase 4 | **於獨立 Session** 實際執行測試與靜態分析，貼回真實 Log |
| **[Liaison] 系統協調官** | 交接點 | 上下文壓縮、確認證據完整、指派下一棒 |

---

## 核心機制一：證據驅動驗證（Evidence-Driven Verification）

> 🔒 **鐵律**：將任務標記為 `[x]` 的**唯一合法條件**，是在 `WORKLOG.md` 出示**本次真實的終端機執行輸出**。

- **可接受的證據**：測試綠燈、`exit code`、錯誤碼、Lint／型別檢查結果、API 回應碼。
- **嚴禁無證據宣稱 Pass**：沒有可複現的 Console Log，狀態一律維持 `Not Run` / `Blocked`，不得打勾。
- 證據不可手寫、不可臆造、不可沿用舊紀錄——必須是本次實際執行的輸出。

每個任務在 `WORKLOG.md` 以固定三欄結構記錄，並附 `<Execution_Evidence>` 區塊貼上原始 Log：

| 測試指令 (Command) | 預期結果 (Expected) | 實際執行證據 (Console Output Snippet) |
|--------------------|---------------------|----------------------------------------|
| `npm test -- --coverage` | 全綠且覆蓋率 ≥ 80% | `Tests 17 passed (17)` … `exit 0` |

```text
<Execution_Evidence>
（此處貼上指令 + stdout/stderr + exit code 的真實輸出）
</Execution_Evidence>
```

---

## 核心機制二：Session 物理隔離協議

> 🚧 **鐵律**：[Builder] 與 [Tester] **嚴禁在同一個對話 Session 中作業**——杜絕球員兼裁判。

交接以**里程碑式授權**進行，透過 `shared/tester_input.json` 跨 Session 傳遞：

```
[Builder Session]                              [Tester Session]（全新對話）
 寫程式 + 寫測試                                 讀取 shared/tester_input.json
   │                                             │
   ├─ 生成 shared/tester_input.json  ──────────▶ 實際執行 test / lint / type-check
   │   { changed_files, commands, expected }     │
   └─ Orchestrator 暫停並提示：                  └─ 將真實 Log 貼回 WORKLOG.md
      「請開啟新的 Session 套用 Tester」              → 全綠才可標記 [x]
```

- **交接檔 `shared/tester_input.json`**：Builder 列出本次變更檔案、應跑的測試指令與預期結果，作為對 Tester 的授權與輸入。
- **Session 斷點**：流程由 Builder 移交 Tester 時，Orchestrator 必須主動**暫停**並輸出標準提示，等待使用者開新 Session，**不得**在同一 Session 自行續測。

`shared/tester_input.json` 範例：

```json
{
  "task": "0.3 核心邏輯模組開發與單元測試",
  "changed_files": ["src/core/foo.js", "test/foo.test.js"],
  "commands": ["npm install", "npm test -- --coverage", "npm run lint"],
  "expected": ["exit 0", "全綠且覆蓋率 >= 80%", "0 error"]
}
```

---

## 標準工作流程

```
Phase 1 [PM]        需求釐清 + 可執行 AC          ─┐
Phase 2 [Architect] Schema / 介面 / 技術棧         │ 規劃（不寫實作碼）
Phase 3 [Builder]   實作 + 自動化測試 → 交接檔     ─┤ 〔Session 斷點〕
Phase 4 [Tester]    獨立 Session 實跑 + 貼證據     ─┘ 證據齊全才 [x]
Phase 5 [Liaison]   壓縮上下文 + 指派下一棒
```

完整交接協議（Handover Protocol）詳見 `ai-sop init` 產生的 `AGENTS.md`。

---

## 專案結構

```
ai_agent_sop_toolkit/
├── pyproject.toml
├── setup.py
├── ai_sop_toolkit/
│   ├── cli.py          ← Click CLI 入口點
│   └── templates/      ← SOP 模板（.tpl / .md）
└── tests/
```

執行測試：

```bash
python -m pytest
```

---

## 為什麼做這個工具

在多個 AI 協作開發專案中，每次都要從零重建任務追蹤、角色定義與交接結構，非常耗時；且舊式以「填寫文件」為完成標準，極易淪為形式主義。本工具箱把一套**證據驅動 + 角色物理隔離**的現代協作做法打包成可重複使用的 CLI，讓新專案一開始就有嚴謹結構，而非從混亂開始。

---

## License

MIT
