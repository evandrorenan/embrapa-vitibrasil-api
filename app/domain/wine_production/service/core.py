from typing import List

from fastapi import Depends

from app.domain.wine_production.model.production import ProductionData


class WineProductionRepository:
    def get_all_wine_production_data(self) -> List[ProductionData]:
        pass


class WineProductionService:
    def __init__(self, wine_production_repository: WineProductionRepository = Depends()):
        self.wine_production_repository = wine_production_repository

    def list_all(self) -> List[ProductionData]:
        return self.wine_production_repository.get_all_wine_production_data()
