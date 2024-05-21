from fastapi import Depends
from app.domain.wine_exports.service.core import WineExportsRepository, WineExportsService
from app.infrastructure.csv_wine_exports_repository import CSVExportDataRepository


def get_csv_production_repo() -> WineProductionRepository:
    return CSVProductionDataRepository()


def get_csv_processing_repo() -> WineProcessingRepository:
    return CSVProcessingDataRepository()


def get_csv_trades_repo() -> WineTradesRepository:
    return CSVTradeDataRepository()


def get_csv_imports_repo() -> WineImportsRepository:
    return CSVImportDataRepository()


def get_csv_exports_repo() -> WineExportsRepository:
    return CSVExportDataRepository()


def get_wine_production_service(repo: WineProductionRepository = Depends(get_csv_production_repo)) -> WineProductionService:
    return WineExportsService(repo)


def get_wine_processing_service(repo: WineProcessingRepository = Depends(get_csv_processing_repo)) -> WineProcessingService:
    return WineExportsService(repo)


def get_wine_trades_service(repo: WineTradesRepository = Depends(get_csv_trades_repo)) -> WineTradesService:
    return WineExportsService(repo)


def get_wine_imports_service(repo: WineImportsRepository = Depends(get_csv_imports_repo)) -> WineImportsService:
    return WineExportsService(repo)


def get_wine_exports_service(repo: WineExportsRepository = Depends(get_csv_exports_repo)) -> WineExportsService:
    return WineExportsService(repo)
