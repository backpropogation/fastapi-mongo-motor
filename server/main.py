from fastapi import FastAPI

from apps.api.views.employee import router
from config import get_settings
from config.logging import configure_logging
from db.connect import connect_to_mongo, close_mongo_connection

settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.version)

app.include_router(router, prefix='/api')

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("startup", configure_logging)

app.add_event_handler("shutdown", close_mongo_connection)
