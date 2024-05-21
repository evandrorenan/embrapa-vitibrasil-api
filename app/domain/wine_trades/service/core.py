from typing import List
from fastapi import Depends
from app.domain.wine_trades.model.trades import TradeData


class WineTradesRepository:
    def get_all_wine_trades_data(self) -> List[TradeData]:
        pass


class WineTradeService:
    def __init__(self, wine_trades_repository: WineTradesRepository = Depends()):
        self.wine_trades_repository = wine_trades_repository

    def list_all(self) -> List[TradeData]:
        return self.wine_trades_repository.get_all_wine_trades_data()
