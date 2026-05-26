from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from myapp.config import settings
import asyncio

engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    #pool_size=5,
    #max_overflow=10
)
async def get_123():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f'{res.first()=}')

asyncio.run(get_123())