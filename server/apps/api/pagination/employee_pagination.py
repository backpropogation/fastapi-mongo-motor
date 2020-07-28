from typing import Optional

from pydantic import BaseModel, validator

from config import get_settings

settings = get_settings()


class EmployeePaginationQueryParams(BaseModel):
    page_size: Optional[int] = 30
    page: Optional[int] = 1

    @validator('page_size')
    def check_page_size(cls, v) -> int:
        if settings.min_page_size <= v <= settings.default_page_size:
            return v
        return settings.default_page_size

    @validator('page')
    def check_page(cls, v) -> int:
        if v < 1:
            return settings.default_page
        return v
