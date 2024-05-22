from typing import List

from pydantic import BaseModel


class ProcessingDataLog(BaseModel):
    year: int
    quantity: int


class ProcessingData(BaseModel):
    id: int
    control: str
    cultivar: str
    processingDataLogs: List[ProcessingDataLog]
