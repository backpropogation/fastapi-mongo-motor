import pymongo
from motor.motor_asyncio import AsyncIOMotorClient

from apps.api.filters import EmployeeFilterParams, EmployeeFilterExpressionBuilder
from apps.api.pagination import EmployeePaginationQueryParams
from apps.employees.models.employee import ManyEmployeeInDb, EmployeeInDb
from config.config import Settings
from db.collections import employee_collection


async def get_filtered_employees(filter_params: EmployeeFilterParams,
                                 db: AsyncIOMotorClient,
                                 settings: Settings,
                                 pagination_params: EmployeePaginationQueryParams) -> ManyEmployeeInDb:
    builder = EmployeeFilterExpressionBuilder(**filter_params.dict())
    sort_by = builder.sort_by
    skip = pagination_params.page_size * (pagination_params.page - 1)
    filter_expr = builder.filter_expression
    rows = db[settings.mongo_db_name][employee_collection].find(
        filter_expr
    ).skip(
        skip
    ).limit(
        pagination_params.page_size
    )
    employees_count = await db[settings.mongo_db_name][employee_collection].count_documents(
        filter_expr
    )
    if sort_by:
        rows = rows.sort(sort_by, pymongo.DESCENDING)  # TODO ADD dynamic asc/desc
    return ManyEmployeeInDb(
        count=employees_count,
        employees=[EmployeeInDb(**row) async for row in rows],
        page=pagination_params.page,
        page_size=pagination_params.page_size
    )
