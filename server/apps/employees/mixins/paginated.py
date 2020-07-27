from pydantic import BaseModel


class PaginatedMixin(BaseModel):
    count: int
    page: int
    page_size: int
