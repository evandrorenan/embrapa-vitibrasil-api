from fastapi import APIRouter, HTTPException
from typing import List
from app.domain.wine_exports.model.exports import ExportData
from app.domain.wine_exports.service.CSVService import CSVService


router = APIRouter()


@router.get("/wine-exports", response_model=List[ExportData])
def get_wine_exports_data():
    try:
        return CSVService.read_csv()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
