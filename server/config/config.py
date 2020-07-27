from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My first FastAPI application"
    api_prefix: str = "/api"
    mongo_db_name: str
    mongo_password: str
    mongo_url: str
    debug: bool
    version: str
    max_pool_size: int
    min_pool_size: int
    default_page_size: int = 30
    min_page_size: int = 10


settings = Settings()


def get_settings():
    return settings
