from decimal import Decimal
from typing import List

from pydantic import BaseModel


class ExportLog(BaseModel):
    year: int
    quantity: Decimal
    price: Decimal


class ExportData(BaseModel):
    id: int
    country: str
    export_logs: List[ExportLog]
