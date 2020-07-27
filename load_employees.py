import asyncio
import json

from apps.employees.models.employee import Employee
from config import get_settings
from db.collections import employee_collection
from db.connect import close_mongo_connection, get_database_connection, connect_to_mongo


async def do_insert():
    settings = get_settings()
    await connect_to_mongo()
    with open('fixtures/employees.json') as file:
        json_file = json.load(file)
        client = await get_database_connection()
        employees = [Employee(**item).dict() for item in json_file]
        await client[settings.mongo_db_name][employee_collection].insert_many(employees)
        await close_mongo_connection()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_insert())
