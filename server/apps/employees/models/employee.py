from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from apps.employees.mixins.db_model import DBModelMixin
from apps.employees.mixins.paginated import PaginatedMixin


class User(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None


class Employee(User):
    email: Optional[str] = None
    company: Optional[str] = None
    join_date: Optional[datetime] = None
    job_title: Optional[str] = None
    salary: Optional[int] = None


class EmployeeInDb(DBModelMixin, Employee):
    pass


class ManyEmployeeInDb(PaginatedMixin):
    employees: List[EmployeeInDb]
