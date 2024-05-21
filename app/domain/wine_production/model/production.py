from typing import List

from pydantic import BaseModel


class ProductionLog(BaseModel):
    year: int
    quantity: int


class ProductionData(BaseModel):
    id: int
    product: str
    groupId: int
    productionLogs: List[ProductionLog]
