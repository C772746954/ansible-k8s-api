from app.database.models import Base
from app.dependencies.database import async_engine
import asyncio

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
asyncio.run(init_db())