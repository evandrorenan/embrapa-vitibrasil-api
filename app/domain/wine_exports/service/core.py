from typing import List

from fastapi import Depends

from app.domain.wine_exports.model.exports import ExportData


class WineExportsRepository:
    def get_all_wine_exports_data(self) -> List[ExportData]:
        pass


class WineExportsService:
    def __init__(self, wine_export_repository: WineExportsRepository = Depends()):
        self.wine_export_repository = wine_export_repository

    def list_all(self) -> List[ExportData]:
        return self.wine_export_repository.get_all_wine_exports_data()
