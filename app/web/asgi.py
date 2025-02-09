import uvicorn
from fastapi import FastAPI
from app.web.routes import router
from app.config.config import config

app = FastAPI(title="NarratoAI-DeepSeek", description="基于 DeepSeek AI 的视频解析 API")

# 注册路由
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host=config.listen_host, port=config.listen_port, reload=config.reload_debug)
