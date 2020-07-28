from enum import IntEnum
from pymongo import ASCENDING, DESCENDING

class SortEnum(IntEnum):
    ASC = ASCENDING
    DESC = DESCENDING


