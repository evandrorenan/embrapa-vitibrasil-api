import csv
from decimal import Decimal
from typing import List

from pydantic import ValidationError

from app.domain.wine_production.model.production import ProductionData, ProductionLog
from app.domain.wine_production.service.core import WineProductionRepository
from app.infrastructure import settings


class CSVProductionDataRepository(WineProductionRepository):
    last_all_caps_id = None

    def get_all_wine_production_data(self) -> List[ProductionData]:
        with open(settings.WINE_PRODUCTION_DATA_FILE_PATH, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            rows = list(csv_reader)

        return [self._process_row(row) for row in rows]

    def _process_row(self, row) -> ProductionData:
        id = row["id"]
        product = row["produto"]
        print(f"_process_row: {id} - {product}")
        group_id = self._get_group_id(id, product)
        production_logs = [self._create_production_log(row, year) for year in range(1970, 2024)]
        return ProductionData(id=id, product=product, groupId=group_id, productionLogs=production_logs)

    def _get_group_id(self, id, product) -> int:
        if product.isupper():
            self.last_all_caps_id = id
            return 0
        return self.last_all_caps_id

    def _create_production_log(self, row, year) -> ProductionLog:
        try:
            return ProductionLog(year=year, quantity=row.get(f"{year}"))
        except ValidationError:
            return ProductionLog(year=year, quantity=Decimal(0))
