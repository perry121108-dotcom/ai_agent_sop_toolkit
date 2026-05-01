import os
import json
from policy_reader import PolicyEnforcer

class BaseAgent:
    def __init__(self, name, policy_enforcer):
        self.name = name
        self.policy = policy_enforcer

    def read_file(self, path):
        print(f"[{self.name}] 嘗試讀取檔案: {path}")
        if self.policy.can_read(self.name, path):
            print(f"  ✅ 權限核准：允許讀取 {path}")
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
            else:
                print("  (檔案尚不存在)")
                return None
        else:
            print(f"  ❌ 權限拒絕：無權讀取 {path}")
            return None

    def write_file(self, path, content):
        print(f"[{self.name}] 嘗試寫入檔案: {path}")
        if self.policy.can_write(self.name, path):
            print(f"  ✅ 權限核准：允許寫入 {path}")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f"  ❌ 權限拒絕：無權寫入 {path}")

    def execute_command(self, command):
        print(f"[{self.name}] 嘗試執行指令: {command}")
        if self.policy.can_execute(self.name, command):
            print(f"  ✅ 權限核准：允許執行 {command}")
            # 實際應用中這裡會呼叫 subprocess
            print("  (模擬執行結果...)")
        else:
            print(f"  ❌ 權限拒絕：無權執行 {command}")


def main():
    # 初始化 Policy Reader，載入 project_policy.md
    policy_path = "project_policy.md"
    print(f"載入權限規劃檔: {policy_path}\n")
    enforcer = PolicyEnforcer(policy_path)

    # 實例化兩個 Agent
    agent_a = BaseAgent("AgentA", enforcer)
    agent_b = BaseAgent("AgentB", enforcer)

    print("--- 測試情境 1：Agent A 寫入記憶，Agent B 讀取記憶 ---")
    memory_path = "shared/memory.json"
    data_to_share = json.dumps({"status": "Agent A completed task 1"})
    
    agent_a.write_file(memory_path, data_to_share)
    print()
    agent_b.read_file(memory_path)
    print("\n----------------------------------------------------")

    print("--- 測試情境 2：Agent B 嘗試執行未授權指令 ---")
    agent_b.execute_command("echo Hello World")
    print("\n----------------------------------------------------")

    print("--- 測試情境 3：Agent A 嘗試存取被 Deny 的敏感目錄 ---")
    agent_a.read_file("C:/Windows/System32/config/SAM")
    print("\n----------------------------------------------------")

    print("--- 測試情境 4：Agent B 將處理結果寫出 ---")
    agent_b.write_file("shared/results/output.txt", "This is the final result from Agent B")
    print("\n----------------------------------------------------")

if __name__ == "__main__":
    main()
