# CLAUDE.md — 專案規範與禁止事項

## 核心準則
- 嚴格遵守 `TASK.md` 順序，一次只處理一個任務。
- 每次開發後必須進行雙軌驗證（自動化測試 + 人工 QA 指引）。
- **任務狀態更新規則**：
  - 開始任務 → 同步將 `TASK.md` 標記為 `[/]`，並在 `WORKLOG.md` 建立該任務條目
  - 完成任務 → 先在 `WORKLOG.md` 貼上真實執行證據，再將 `TASK.md` 標記為 `[x]`

## 🔒 證據鐵律（Evidence-Driven Verification）
- 標記任務為 `[x]` 的**唯一合法條件**：在 `WORKLOG.md` 貼上**終端機的真實執行輸出**（測試綠燈、exit code、錯誤碼、Lint／型別檢查結果、API 回應碼等）。
- **嚴禁無證據宣稱 Pass**：沒有可複現的 Console Log，一律視為 `Not Run`，不得標 `[x]`。
- 證據必須是**本次實際執行**所產生的輸出，不可手寫、不可臆造、不可沿用舊紀錄。
- 無法執行的項目一律標 `Blocked` 並說明原因，不得偽裝為 Pass。

## 🚧 隔離鐵律（Builder / Tester Session Isolation）
- Builder（實作）與 Tester（驗證）**嚴禁在同一個對話 Session 中作業**——杜絕球員兼裁判。
- 角色切換必須透過**交接檔** `shared/tester_input.json` 完成，並由使用者**開啟全新 Session** 後再套用對方角色。
- 同一 Session 內**不得**自行從 Builder 切換為 Tester 後自評通過。

## WORKLOG.md 填寫規定
- 每個任務進入 `[/]` 時，必須在 `WORKLOG.md` 建立對應條目並填入負責人（Builder）與開始時間。
- 每筆驗證須填寫「測試指令 / 預期結果 / 實際執行證據」三欄，並在 `<Execution_Evidence>` 區塊貼上真實 Log。
- 未在 `WORKLOG.md` 留下可複現的執行證據前，**不得**將任務標記為 `[x]`。

## ❌ 禁止事項
- 不可跳過測試直接勾選任務。
- 不可在未釐清需求前直接更改核心架構。
- 嚴禁使用硬編碼 (Hard-coded) 敏感資訊。
- 不可在 `WORKLOG.md` 無真實執行證據的情況下標記任務為 `[x]`。
- 不可在同一個 Session 中身兼 Builder 與 Tester。
