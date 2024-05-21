import csv
from decimal import Decimal
from typing import List

from pydantic import ValidationError

from app.domain.wine_trades.model.trades import TradeData, TradeDataLog
from app.domain.wine_trades.service.core import WineTradesRepository
from app.infrastructure import settings


class CSVTradeDataRepository(WineTradesRepository):
    def get_all_wine_trades_data(self) -> List[TradeData]:
        with open(settings.WINE_TRADES_FILE_PATH, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            rows = list(csv_reader)

        return [CSVTradeDataRepository._process_row(row) for row in rows]

    @staticmethod
    def _process_row(row) -> TradeData:
        control = row["Produto"]
        product = row["control"]
        trade_logs = [CSVTradeDataRepository._create_trade_log(row, year) for year in range(1970, 2024)]
        return TradeData(id=row["id"], control=control, product=product, tradeDataLogs=trade_logs)

    @staticmethod
    def _create_trade_log(row, year) -> TradeDataLog:
        try:
            return TradeDataLog(year=year, quantity=row.get(f"{year}"))
        except ValidationError:
            return TradeDataLog(year=year, quantity=Decimal(0))
