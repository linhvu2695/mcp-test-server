from pydantic import BaseModel
from enum import Enum

class Operator(Enum):
    EQUAL = ":"
    GREATER_THAN = ">"
    LESS_THAN = "<"

class Criterion(BaseModel):
    field: str
    value: str
    operator: Operator

class SearchRequest(BaseModel):
    criteria: list[Criterion]
    returned_fields: list[str]