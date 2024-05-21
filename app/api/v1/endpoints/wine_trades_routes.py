from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.di.dependencies import get_wine_exports_service
from app.domain.wine_trades.service.core import WineTradeService
from app.domain.wine_trades.model.trades import TradeData

router = APIRouter()


@router.get("/wine-trades", response_model=List[TradeData])
def get_wine_trades_data(service: WineTradeService = Depends(get_wine_exports_service)):
    try:
        return service.list_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
