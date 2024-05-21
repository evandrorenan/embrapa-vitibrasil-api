from typing import List

from fastapi import Depends

from app.domain.wine_imports.model.imports import ImportData


class WineImportsRepository:
    def get_all_wine_imports_data(self) -> List[ImportData]:
        pass


class WineImportService:
    def __init__(self, wine_imports_repository: WineImportsRepository = Depends()):
        self.wine_imports_repository = wine_imports_repository

    def list_all(self) -> List[ImportData]:
        return self.wine_imports_repository.get_all_wine_imports_data()
