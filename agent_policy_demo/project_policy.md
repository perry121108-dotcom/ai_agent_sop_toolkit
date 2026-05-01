# Agent Project Policy

這是一份用來控制本地 Agent 權限的規劃檔。
Agent 在執行任何動作前，都必須先讀取並遵循此規劃檔的設定。

## Permissions

```yaml
permissions:
  AgentA:
    allow_read:
      - "shared/logs/*"
    allow_write:
      - "shared/memory.json"
    allow_execute:
      - "echo"
      - "dir"
    deny:
      - "C:/Windows/*"
      - "~/.ssh/*"
  AgentB:
    allow_read:
      - "shared/memory.json"
    allow_write:
      - "shared/results/*"
    allow_execute: []
    deny:
      - "C:/Windows/*"
      - "~/.ssh/*"
```
