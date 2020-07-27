from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from apps.employees.models.employee import ManyEmployeeInDb


def create_response(model: ManyEmployeeInDb, status_code: int = status.HTTP_200_OK) -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(model), status_code=status_code)
