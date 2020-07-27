from fastapi import Depends
from fastapi.requests import Request
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from apps.api.filters import EmployeeFilterParams
from apps.api.pagination import EmployeePaginationQueryParams
from apps.api.routers import router
from apps.api.utils.create_response import create_response
from apps.api.utils.get_filtered_employees import get_filtered_employees
from apps.employees.models.employee import ManyEmployeeInDb
from config.config import get_settings, Settings
from db.connect import get_database_connection


@router.get("/", response_model=ManyEmployeeInDb)
async def employee_list(request: Request,
                        filter_params: EmployeeFilterParams = Depends(),
                        db: AsyncIOMotorClient = Depends(get_database_connection),
                        pagination_params: EmployeePaginationQueryParams = Depends(),
                        settings: Settings = Depends(get_settings),
                        ):
    logger.debug(f"Request from {request.client.host} with query params: {request.query_params}")
    employees = await get_filtered_employees(filter_params, db, settings, pagination_params)
    logger.debug(f"Got {employees.count} employees.")
    return create_response(model=employees)
