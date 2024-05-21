from typing import List
from app.domain.wine_exports.model.exports import ExportData
from fastapi import Depends


class WineExportsRepository:
    def get_all_wine_exports_data(self) -> List[ExportData]:
        pass


class WineExportsService:
    def __init__(self, wine_export_repository: WineExportsRepository = Depends()):
        self.wine_export_repository = wine_export_repository

    def list_all(self) -> List[ExportData]:
        return self.wine_export_repository.get_all_wine_exports_data()
