from app.models.deepseek import deepseek

class VideoAnalyzer:
    def __init__(self, video_url):
        self.video_url = video_url

    def analyze(self):
        """解析视频内容并返回文本摘要"""
        try:
            result = deepseek.analyze_video(self.video_url)
            return result.get("summary", "No summary available.")
        except Exception as e:
            return f"Error analyzing video: {str(e)}"

# 测试调用
if __name__ == "__main__":
    video_url = "https://example.com/video.mp4"
    analyzer = VideoAnalyzer(video_url)
    print(analyzer.analyze())
