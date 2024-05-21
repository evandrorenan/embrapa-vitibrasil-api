from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.di.dependencies import get_wine_exports_service
from app.domain.wine_exports.model.exports import ExportData
from app.domain.wine_exports.service.core import WineExportsService

router = APIRouter()


@router.get("/wine-exports", response_model=List[ExportData])
def get_wine_exports_data(service: WineExportsService = Depends(get_wine_exports_service)):
    try:
        return service.list_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
