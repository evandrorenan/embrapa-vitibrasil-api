from typing import List
from pydantic import BaseModel
from decimal import Decimal


class Quantity(BaseModel):
    quantity: Decimal


class Year(BaseModel):
    year: int
    quantity: Quantity


class TradeData(BaseModel):
    id: int
    country: str
    years: List[Year]
