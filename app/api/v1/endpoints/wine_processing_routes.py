from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.di.dependencies import get_wine_processing_service
from app.domain.wine_processing.model.processing import ProcessingData
from app.domain.wine_processing.service.core import WineProcessingService

router = APIRouter()


@router.get("/wine-processing", response_model=List[ProcessingData])
def get_wine_processing_data(service: WineProcessingService = Depends(get_wine_processing_service)):
    try:
        return service.list_all()
    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))
