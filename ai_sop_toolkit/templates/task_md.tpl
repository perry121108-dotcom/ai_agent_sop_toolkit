# 開發任務進度表 (TASK.md)

## 狀態說明
- `[ ]` 未開始
- `[/]` 進行中（Builder 已產出實作與測試腳本，待 Tester 於獨立 Session 驗證）
- `[x]` 已完成（須在 `WORKLOG.md` 附上真實執行證據才可標記）

## ✅ AC（驗收標準）撰寫規範
- AC 必須寫成**可執行的指令或自動化斷言**，能被 Tester 直接貼進終端機執行並得到客觀結果。
- ✅ 範例（合法）：`npm run test` 全綠（exit 0）、`npm run lint` 0 error、`curl -s -o /dev/null -w "%{http_code}" /api/health` 回傳 `200`、`pytest -q` 通過、覆蓋率 ≥ 80%（報表數字為證）。
- ❌ 禁止（模糊自然語言）：「功能正常」「回傳符合規格」「邊界有處理」等無法機器驗證的描述。
- 每條 AC 都要能對應到 `WORKLOG.md` 中一列「測試指令 + 預期結果 + 實際執行證據」。

---

## P0: 基礎環境與核心架構

- [ ] **0.1** 初始化專案結構與依賴安裝
  - AC: `npm install` exit 0；`npm run build` exit 0（或對應啟動指令成功）
- [ ] **0.2** 資料庫 Schema 建立與驗證
  - AC: `npm run migrate:up` 與 `npm run migrate:down` 皆 exit 0；schema 驗證腳本通過
- [ ] **0.3** 核心邏輯模組開發與單元測試
  - AC: `npm test -- --coverage` 全數通過且覆蓋率 ≥ 80%（報表數字為證）

## P1: 業務功能開發

- [ ] **1.1** 實作 API 路由 / UI 組件
  - AC: `npm test path/to/api.test.js` 通過；正常請求回 `200`、缺欄位回 `400`
- [ ] **1.2** 整合驗證機制（如 JWT/Session）
  - AC: 未授權請求 `curl` 回 `401`；過期 Token 測試案例通過（測試輸出為證）

---

> 新增任務格式：
> `- [ ] **X.X** 任務名稱`
> `  - AC: <可執行指令或自動化斷言，例：npm test 通過 / 回傳 200>`
