from motor.motor_asyncio import AsyncIOMotorClient

from config import get_settings
from loguru import logger


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database_connection() -> AsyncIOMotorClient:
    return db.client


async def connect_to_mongo():
    logger.info("Connecting to mongo...")
    settings = get_settings()
    db.client = AsyncIOMotorClient(
        settings.mongo_url,
        maxPoolSize=settings.max_pool_size,
        minPoolSize=settings.min_pool_size
    )
    logger.info("Connected to mongo successfully")


async def close_mongo_connection():
    logger.info("Closing mongo connection...")
    db.client.close()
    logger.info("Closed mongo connection successfully")
