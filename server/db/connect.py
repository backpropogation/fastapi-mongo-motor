from motor.motor_asyncio import AsyncIOMotorClient

from config import get_settings


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database_connection() -> AsyncIOMotorClient:
    return db.client


async def connect_to_mongo():
    settings = get_settings()
    db.client = AsyncIOMotorClient(
        settings.mongo_url,
        maxPoolSize=settings.max_pool_size,
        minPoolSize=settings.min_pool_size
    )


async def close_mongo_connection():
    db.client.close()
