from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from starlette import status
from starlette.responses import JSONResponse

from apps.api.filters import EmployeeFilterParams
from apps.api.pagination import EmployeePaginationQueryParams
from apps.api.routers import router
from apps.api.utils.get_filtered_employees import get_filtered_employees
from apps.employees.models.employee import ManyEmployeeInDb
from config.config import get_settings, Settings
from db.connect import get_database_connection


def create_response(model: ManyEmployeeInDb, status_code: int = status.HTTP_200_OK) -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(model), status_code=status_code)


@router.get("/", response_model=ManyEmployeeInDb)
async def employee_list(filter_params: EmployeeFilterParams = Depends(),
                        db: AsyncIOMotorClient = Depends(get_database_connection),
                        pagination_params: EmployeePaginationQueryParams = Depends(),
                        settings: Settings = Depends(get_settings)):
    employees = await get_filtered_employees(filter_params, db, settings, pagination_params)
    return create_response(model=employees)
