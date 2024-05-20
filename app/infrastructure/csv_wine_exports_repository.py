import csv
from typing import List
from app.core.settings import settings
from app.domain.wine_exports.model.exports import ExportData, ExportLog
from app.domain.wine_exports.service.wine_exports_service import WineExportsRepository
from decimal import Decimal


class CSVExportDataRepository(WineExportsRepository):
    def get_all_wine_exports_data(self) -> List[ExportData]:
        with open(settings.EXPORT_FILE_PATH, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            rows = list(csv_reader)

        return [CSVExportDataRepository._process_row(row) for row in rows]

    @staticmethod
    def _process_row(row) -> ExportData:
        export_logs = [CSVExportDataRepository._create_export_log(row, year) for year in range(1970, 2024)]
        return ExportData(id=row["Id"], country=row["País"], export_logs=export_logs)

    @staticmethod
    def _create_export_log(row, year) -> ExportLog:
        try:
            return ExportLog(year=year, quantity=row.get(f"{year}_q"), price=row.get(f"{year}_v"))
        except Exception as e:
            print(f"No content for {row['Id']}-{year}. Error thrown: {e}")
            return ExportLog(year=year, quantity=Decimal("0"), price=Decimal("0"))
