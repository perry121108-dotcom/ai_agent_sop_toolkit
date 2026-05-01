import os
import yaml
import fnmatch
from pathlib import Path

class PolicyEnforcer:
    def __init__(self, policy_md_path):
        self.policy_md_path = policy_md_path
        self.policies = self._load_policies()

    def _load_policies(self):
        """從 project_policy.md 中萃取 YAML 區塊並解析"""
        if not os.path.exists(self.policy_md_path):
            raise FileNotFoundError(f"Policy file not found: {self.policy_md_path}")
            
        with open(self.policy_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 簡單萃取 ```yaml 和 ``` 之間的內容
        yaml_start = content.find("```yaml")
        if yaml_start == -1:
            raise ValueError("No YAML block found in policy file")
            
        yaml_start += len("```yaml\n")
        yaml_end = content.find("```", yaml_start)
        yaml_content = content[yaml_start:yaml_end].strip()
        
        parsed = yaml.safe_load(yaml_content)
        return parsed.get("permissions", {})

    def _is_path_allowed(self, path, allowed_patterns):
        """檢查路徑是否符合允許的模式"""
        # 將路徑標準化，並使用 fnmatch 進行萬用字元比對
        path = os.path.normpath(path).replace('\\', '/')
        for pattern in allowed_patterns:
            pattern = os.path.normpath(pattern).replace('\\', '/')
            if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(path, pattern + "/*"):
                return True
        return False

    def can_read(self, agent_name, path):
        """檢查 Agent 是否被允許讀取該路徑"""
        agent_policy = self.policies.get(agent_name, {})
        
        # 先檢查 deny list
        if self._is_path_allowed(path, agent_policy.get("deny", [])):
            return False
            
        # 再檢查 allow_read list
        return self._is_path_allowed(path, agent_policy.get("allow_read", []))

    def can_write(self, agent_name, path):
        """檢查 Agent 是否被允許寫入該路徑"""
        agent_policy = self.policies.get(agent_name, {})
        
        # 先檢查 deny list
        if self._is_path_allowed(path, agent_policy.get("deny", [])):
            return False
            
        # 再檢查 allow_write list
        return self._is_path_allowed(path, agent_policy.get("allow_write", []))

    def can_execute(self, agent_name, command):
        """檢查 Agent 是否被允許執行該指令"""
        agent_policy = self.policies.get(agent_name, {})
        
        allowed_cmds = agent_policy.get("allow_execute", [])
        base_cmd = command.split()[0] if command else ""
        
        return base_cmd in allowed_cmds
