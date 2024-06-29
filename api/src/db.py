from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+aiomysql://root@mysql:3306/mydb?charset=utf8"

db_engine = create_async_engine(DB_URL, echo=True)
db_session = sessionmaker(
    autocommit=False, autoflush=False, bind=db_engine, class_=AsyncSession
)


async def get_db():
    async with db_session() as session:
        yield session
