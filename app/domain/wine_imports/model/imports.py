from decimal import Decimal
from typing import List

from pydantic import BaseModel


class ImportLog(BaseModel):
    year: int
    quantity: Decimal
    price: Decimal


class ImportData(BaseModel):
    id: int
    country: str
    import_logs: List[ImportLog]
