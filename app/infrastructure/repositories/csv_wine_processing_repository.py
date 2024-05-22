import csv
from decimal import Decimal
from typing import List

from pydantic import ValidationError

from app.domain.wine_processing.model.processing import ProcessingData, ProcessingDataLog
from app.domain.wine_processing.service.core import WineProcessingRepository
from app.infrastructure import settings


class CSVProcessingDataRepository(WineProcessingRepository):
    def get_all_wine_processing_data(self) -> List[ProcessingData]:
        with open(settings.WINE_PROCESSING_DATA_FILE_PATH, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            rows = list(csv_reader)

        return [CSVProcessingDataRepository._process_row(row) for row in rows]

    @staticmethod
    def _process_row(row) -> ProcessingData:
        control = row["control"]
        cultivar = row["cultivar"]
        processing_logs = [CSVProcessingDataRepository._create_processing_log(row, year) for year in range(1970, 2024)]
        return ProcessingData(id=row["id"], control=control, cultivar=cultivar, processingDataLogs=processing_logs)

    @staticmethod
    def _create_processing_log(row, year) -> ProcessingDataLog:
        try:
            return ProcessingDataLog(year=year, quantity=row.get(f"{year}"))
        except ValidationError:
            return ProcessingDataLog(year=year, quantity=Decimal(0))
