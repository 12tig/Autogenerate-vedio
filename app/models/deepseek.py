import requests
from app.config.config import config

class DeepSeekAPI:
    BASE_URL = "https://api.deepseek.com/v1/video/analyze"

    def __init__(self):
        self.api_key = config.deepseek_api_key
        if not self.api_key:
            raise ValueError("DeepSeek API Key is missing in config!")

    def analyze_video(self, video_url):
        """调用 DeepSeek 进行视频内容分析"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "video_url": video_url
        }

        response = requests.post(self.BASE_URL, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()  # 返回解析结果
        else:
            raise Exception(f"DeepSeek API Error: {response.text}")

deepseek = DeepSeekAPI()
