from fastapi.middleware.cors import CORSMiddleware
from app.routers import configmaps_router, auth_router
from fastapi import FastAPI
from app.dependencies.database import async_engine
from app.database.models import Base
import logging
import asyncio

# 定义全局 logger
logger = logging.getLogger(__name__)

# 初始化应用
app = FastAPI(title="K8S Manager", version="1.0")

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(configmaps_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/auth")

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 数据库初始化
@app.on_event("startup")
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database initialized")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)