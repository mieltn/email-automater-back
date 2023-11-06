from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from core.settings import get_app_settings

Base = declarative_base()
SETTINGS = get_app_settings()

async_engine = create_async_engine(
    url=SETTINGS.async_postgres_dsn,
    future=True,
)

async_session = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)