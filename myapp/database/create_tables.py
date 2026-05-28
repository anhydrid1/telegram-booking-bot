import asyncio

from myapp.database.db import engine
from myapp.database.models import Base

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Запускать так: python -m myapp.database.create_tables
if __name__ == '__main__':
    asyncio.run(main())
