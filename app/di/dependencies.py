from fastapi import Depends
from app.domain.wine_exports.service.core import WineExportsRepository, WineExportService
from app.infrastructure.csv_wine_exports_repository import CSVExportDataRepository


def get_csv_repository() -> WineExportsRepository:
    return CSVExportDataRepository()


def get_service(repo: WineExportsRepository = Depends(get_csv_repository)) -> WineExportService:
    return WineExportService(repo)
