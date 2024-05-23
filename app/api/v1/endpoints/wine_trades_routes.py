from typing import List

from fastapi import APIRouter, HTTPException, Depends

from app.di.dependencies import get_wine_trades_service
from app.domain.wine_trades.model.trades import TradeData
from app.domain.wine_trades.service.core import WineTradeService

router = APIRouter()


@router.get("/wine-trades", response_model=List[TradeData])
def get_wine_trades_data(service: WineTradeService = Depends(get_wine_trades_service)):
    try:
        return service.list_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
