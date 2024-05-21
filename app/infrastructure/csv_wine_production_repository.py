import csv
from typing import List
from pydantic import ValidationError
from app.domain.wine_production.model.production import ProductionData, ProductionLog
from app.domain.wine_production.service.core import WineProductionRepository
from decimal import Decimal

from app.infrastructure import settings


class CSVProductionDataRepository(WineProductionRepository):
    def get_all_wine_production_data(self) -> List[ProductionData]:
        with open(settings.WINE_PRODUCTION_DATA_FILE_PATH, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            rows = list(csv_reader)

        return [CSVProductionDataRepository._process_row(row) for row in rows]

    @staticmethod
    def _process_row(row) -> ProductionData:
        export_logs = [CSVProductionDataRepository._create_export_log(row, year) for year in range(1970, 2024)]
        return ProductionData(id=row["Id"], country=row["País"], export_logs=export_logs)

    @staticmethod
    def _create_export_log(row, year) -> ProductionLog:
        try:
            return ProductionLog(year=year, quantity=row.get(f"{year}_q"), price=row.get(f"{year}_v"))
        except ValidationError:
            return ProductionLog(year=year, quantity=Decimal(0), price=Decimal(0))
