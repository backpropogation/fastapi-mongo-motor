from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel, root_validator

from apps.api.filters import FilterExpressionBuilder


class EmployeeFilterParams(BaseModel):
    age: int = None
    age_gt: Optional[int] = None
    age_lt: Optional[int] = None

    name: Optional[str] = None

    email: Optional[str] = None

    job_title: Optional[str] = None

    company: Optional[str] = None

    join_date: Optional[datetime] = None
    join_date_gt: Optional[datetime] = None
    join_date_lt: Optional[datetime] = None

    salary: Optional[int] = None
    salary_lt: Optional[int] = None
    salary_gt: Optional[int] = None

    gender: Optional[str] = None
    sort_by: Optional[str] = None


class EmployeeFilterExpressionBuilder(FilterExpressionBuilder, EmployeeFilterParams):
    main_fields: tuple = ('age', 'name', 'job_title', 'company', 'salary', 'gender', 'join_date', "email")

    @root_validator
    def check_sort_by(cls, values) -> str:
        sort_by = values.get('sort_by')
        if sort_by and sort_by not in values:
            values['sort_by'] = None
        return values

    def _get_query_filter_expression(self) -> dict:
        filter_expression = {}
        for field_name in self.main_fields:
            value = getattr(self, field_name)
            if isinstance(value, str):
                filter_expression.update(self._get_string_filter_expr(value, field_name))
            else:
                filter_expression.update(self._get_gt_lt_filter_expr(value, field_name))
        return filter_expression

    @property
    def filter_expression(self) -> dict:
        return self._get_query_filter_expression()

    # noinspection PyMethodMayBeStatic
    def _get_string_filter_expr(self, value: str, field_name: str) -> dict:
        if value:
            return {
                f"{field_name}": {"$regex": f".*{value}.*"}
            }
        return {}

    def _get_gt_lt_filter_expr(self, value: Any, field_name: str) -> dict:
        filter_query = {}
        field_gt = getattr(self, f"{field_name}_gt", None)
        field_lt = getattr(self, f"{field_name}_lt", None)
        if field_gt and field_lt:
            filter_query[field_name] = {"$lt": field_lt, "$gt": field_gt}
        elif field_gt:
            filter_query[field_name] = {"$gt": field_gt}
        elif field_lt:
            filter_query[field_name] = {"$lt": field_lt}
        elif value:
            filter_query[field_name] = value
        return filter_query
