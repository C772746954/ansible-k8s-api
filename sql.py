from app.database.models import User
from app.dependencies.database import async_engine
from sqlalchemy import insert
import asyncio

async def create_user():
    async with async_engine.connect() as conn:
        await conn.execute(
            insert(User).values(
                username="admin",
                hashed_password="\$2b\$12\$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPVgaYl5O"  # 密码明文为 "secret"
            )
        )
        await conn.commit()

asyncio.run(create_user())


