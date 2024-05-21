import csv
from typing import List

from pydantic import ValidationError

from app.domain.wine_trades.model.trades import TradeData, TradeLog
from app.domain.wine_trades.service.core import WineTradesRepository
from decimal import Decimal

from app.infrastructure import settings


class CSVTradeDataRepository(WineTradesRepository):
    def get_all_wine_trades_data(self) -> List[TradeData]:
        with open(settings.WINE_TRADES_FILE_PATH, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            rows = list(csv_reader)

        return [CSVTradeDataRepository._process_row(row) for row in rows]

    @staticmethod
    def _process_row(row) -> TradeData:
        trade_logs = [CSVTradeDataRepository._create_trade_log(row, year) for year in range(1970, 2024)]
        return TradeData(id=row["Id"], country=row["País"], trade_logs=trade_logs)

    @staticmethod
    def _create_trade_log(row, year) -> TradeLog:
        try:
            return TradeLog(year=year, quantity=row.get(f"{year}_q"), price=row.get(f"{year}_v"))
        except ValidationError:
            return TradeLog(year=year, quantity=Decimal(0), price=Decimal(0))
