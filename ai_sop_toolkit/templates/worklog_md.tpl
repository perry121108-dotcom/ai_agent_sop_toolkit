# 工作紀錄 (WORKLOG.md)

> 規則：任務標為 `[x]` 前，對應條目必須附上**真實的終端機執行證據**（見 CLAUDE.md 證據鐵律）。
> 「實際執行證據」欄與 `<Execution_Evidence>` 區塊不得留空、不得手寫臆造、不得沿用舊 Log。
> Builder 在自身 Session 撰寫程式與測試；Tester 在**全新隔離 Session** 實際執行並貼回證據。

---

## 0.1 初始化專案結構與依賴安裝
**狀態**：[ ] | **Builder**： | **Tester**： | **完成時間**：

| 測試指令 (Command) | 預期結果 (Expected) | 實際執行證據 (Console Output Snippet) |
|--------------------|---------------------|----------------------------------------|
| `npm install` | exit code 0、無錯誤 |  |
| `npm run build` | exit code 0 |  |

<Execution_Evidence>
```text
（Tester 在此貼上實際終端機輸出：指令 + stdout/stderr + exit code）
```
</Execution_Evidence>

---

## 0.2 資料庫 Schema 建立與驗證
**狀態**：[ ] | **Builder**： | **Tester**： | **完成時間**：

| 測試指令 (Command) | 預期結果 (Expected) | 實際執行證據 (Console Output Snippet) |
|--------------------|---------------------|----------------------------------------|
| `npm run migrate:up` | exit code 0 |  |
| `npm run migrate:down` | exit code 0 |  |

<Execution_Evidence>
```text
（貼上 migration up/down 的真實輸出）
```
</Execution_Evidence>

---

## 0.3 核心邏輯模組開發與單元測試
**狀態**：[ ] | **Builder**： | **Tester**： | **完成時間**：

| 測試指令 (Command) | 預期結果 (Expected) | 實際執行證據 (Console Output Snippet) |
|--------------------|---------------------|----------------------------------------|
| `npm test -- --coverage` | 全數通過且覆蓋率 ≥ 80% |  |
| `npm run lint` | 0 error |  |

<Execution_Evidence>
```text
（貼上測試與覆蓋率報表、Lint 的真實輸出）
```
</Execution_Evidence>

---

## 1.1 實作 API 路由 / UI 組件
**狀態**：[ ] | **Builder**： | **Tester**： | **完成時間**：

| 測試指令 (Command) | 預期結果 (Expected) | 實際執行證據 (Console Output Snippet) |
|--------------------|---------------------|----------------------------------------|
| `npm test path/to/api.test.js` | 全綠通過 |  |
| `curl -s -o /dev/null -w "%{http_code}" /api/...` | 正常請求 `200`、缺欄位 `400` |  |

<Execution_Evidence>
```text
（貼上 API 測試與 curl 狀態碼的真實輸出）
```
</Execution_Evidence>

---

## 1.2 整合驗證機制
**狀態**：[ ] | **Builder**： | **Tester**： | **完成時間**：

| 測試指令 (Command) | 預期結果 (Expected) | 實際執行證據 (Console Output Snippet) |
|--------------------|---------------------|----------------------------------------|
| `curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer bad" /api/...` | 回傳 `401` |  |
| `npm test path/to/auth.test.js` | 過期 Token 案例通過 |  |

<Execution_Evidence>
```text
（貼上未授權／過期 Token 測試的真實輸出）
```
</Execution_Evidence>

---

> 新增任務格式：
> `## X.X 任務名稱`
> `**狀態**：[ ] | **Builder**： | **Tester**： | **完成時間**：`
> 固定表格欄位：`測試指令 (Command) | 預期結果 (Expected) | 實際執行證據 (Console Output Snippet)`
> 並附 `<Execution_Evidence>` 區塊貼上真實 Log。
