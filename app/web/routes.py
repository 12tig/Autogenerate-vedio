from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.processing.video_analyzer import VideoAnalyzer

router = APIRouter()

# 定义请求数据格式
class VideoRequest(BaseModel):
    video_url: str

@router.post("/analyze_video")
async def analyze_video(request: VideoRequest):
    """接收视频 URL，并返回解析结果"""
    try:
        analyzer = VideoAnalyzer(request.video_url)
        result = analyzer.analyze()
        return {"status": "success", "summary": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
