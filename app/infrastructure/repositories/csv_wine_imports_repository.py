import csv
from decimal import Decimal
from typing import List

from pydantic import ValidationError

from app.domain.wine_imports.model.imports import ImportData, ImportLog
from app.domain.wine_imports.service.core import WineImportsRepository
from app.infrastructure import settings


class CSVImportDataRepository(WineImportsRepository):
    def get_all_wine_imports_data(self) -> List[ImportData]:
        with open(settings.WINE_EXPORT_FILE_PATH, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            rows = list(csv_reader)

        return [CSVImportDataRepository._process_row(row) for row in rows]

    @staticmethod
    def _process_row(row) -> ImportData:
        import_logs = [CSVImportDataRepository._create_import_log(row, year) for year in range(1970, 2024)]
        return ImportData(id=row["Id"], country=row["País"], import_logs=import_logs)

    @staticmethod
    def _create_import_log(row, year) -> ImportLog:
        try:
            return ImportLog(year=year, quantity=row.get(f"{year}_q"), price=row.get(f"{year}_v"))
        except ValidationError:
            return ImportLog(year=year, quantity=Decimal(0), price=Decimal(0))
