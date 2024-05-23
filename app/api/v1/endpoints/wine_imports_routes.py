from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.di.dependencies import get_wine_imports_service
from app.domain.wine_imports.model.imports import ImportData
from app.domain.wine_imports.service.core import WineImportService

router = APIRouter()


@router.get("/wine-imports", response_model=List[ImportData])
def get_wine_imports_data(service: WineImportService = Depends(get_wine_imports_service)):
    try:
        return service.list_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
