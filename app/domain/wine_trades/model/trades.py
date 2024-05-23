from typing import List

from pydantic import BaseModel


class TradeDataLog(BaseModel):
    year: int
    quantity: int


class TradeData(BaseModel):
    id: int
    control: str
    product: str
    tradeDataLogs: List[TradeDataLog]
