from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from myapp.config import settings


engine = create_async_engine(
    url=settings.database_url,
    echo=True
)

async_session = async_sessionmaker(engine)

