from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.di.dependencies import get_wine_production_service
from app.domain.wine_production.model.production import ProductionData
from app.domain.wine_production.service.core import WineProductionService

router = APIRouter()


@router.get("/wine-production", response_model=List[ProductionData])
def get_wine_production_data(service: WineProductionService = Depends(get_wine_production_service)):
    try:
        return service.list_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
