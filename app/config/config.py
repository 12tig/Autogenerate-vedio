import toml
import os

class Config:
    def __init__(self, config_path="config.toml"):
        if os.path.exists(config_path):
            self.config = toml.load(config_path)
        else:
            raise FileNotFoundError(f"Config file '{config_path}' not found!")

        # 读取代理设置（如果有的话）
        self.proxy = self.config.get("proxy", {})
        
        # 读取服务器设置
        self.listen_host = self.config.get("server", {}).get("host", "127.0.0.1")
        self.listen_port = self.config.get("server", {}).get("port", 8000)
        self.reload_debug = self.config.get("server", {}).get("reload", False)

        # DeepSeek API 配置
        self.deepseek_api_key = self.config.get("deepseek", {}).get("api_key", "")

config = Config()
