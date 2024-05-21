from fastapi import Depends

from app.domain.wine_exports.service.core import WineExportsRepository, WineExportsService
from app.domain.wine_imports.service.core import WineImportsRepository, WineImportService
from app.domain.wine_processing.service.core import WineProcessingRepository, WineProcessingService
from app.domain.wine_production.service.core import WineProductionRepository, WineProductionService
from app.domain.wine_trades.service.core import WineTradesRepository, WineTradeService
from app.infrastructure.repositories.csv_wine_exports_repository import CSVExportDataRepository
from app.infrastructure.repositories.csv_wine_imports_repository import CSVImportDataRepository
from app.infrastructure.repositories.csv_wine_processing_repository import CSVProcessingDataRepository
from app.infrastructure.repositories.csv_wine_production_repository import CSVProductionDataRepository
from app.infrastructure.repositories.csv_wine_trades_repository import CSVTradeDataRepository


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


def get_wine_production_service(
        repo: WineProductionRepository = Depends(get_csv_production_repo)) -> WineProductionService:
    return WineProductionService(repo)


def get_wine_processing_service(
        repo: WineProcessingRepository = Depends(get_csv_processing_repo)) -> WineProcessingService:
    return WineProcessingService(repo)


def get_wine_trades_service(repo: WineTradesRepository = Depends(get_csv_trades_repo)) -> WineTradeService:
    return WineTradeService(repo)


def get_wine_imports_service(repo: WineImportsRepository = Depends(get_csv_imports_repo)) -> WineImportService:
    return WineImportService(repo)


def get_wine_exports_service(repo: WineExportsRepository = Depends(get_csv_exports_repo)) -> WineExportsService:
    return WineExportsService(repo)
