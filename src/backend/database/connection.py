from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

DATABASE_URL = ""


Base = declarative_base()
# metadata = MetaData()


# engine = create_async_engine(DATABASE_URL, poolclass=NullPool)
# async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
#
#
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session


class AsyncDatabaseSession:
    def __init__(self):
        self.engine = None
        self.session = None
        self.metadata = MetaData()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(AsyncDatabaseSession, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    async def init_db(self):
        self.engine = create_async_engine(DATABASE_URL, future=True, echo=True)
        self.session = sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=False)

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(self.metadata.create_all)

    async def close_db(self):
        if self.session:
            await self.session.close()
        if self.engine:
            await self.engine.dispose()


db = AsyncDatabaseSession()


async def commit_rollback():
    try:
        await db.session.commit()
    except Exception:
        await db.session.rollback()
        raise
    finally:
        await db.session.close()
