from typing import List

from fastapi import Depends

from app.domain.wine_processing.model.processing import ProcessingData


class WineProcessingRepository:
    def get_all_wine_processing_data(self) -> List[ProcessingData]:
        pass


class WineProcessingService:
    def __init__(self, wine_processing_repository: WineProcessingRepository = Depends()):
        self.wine_processing_repository = wine_processing_repository

    def list_all(self) -> List[ProcessingData]:
        return self.wine_processing_repository.get_all_wine_processing_data()
