from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.di.dependencies import get_service
from app.domain.wine_exports.model.exports import ExportData
from app.domain.wine_exports.service.core import WineExportService, WineExportsRepository


router = APIRouter()


@router.get("/wine-exports", response_model=List[ExportData])
def get_wine_exports_data(service: WineExportService = Depends(get_service)):
    try:
        return service.list_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
