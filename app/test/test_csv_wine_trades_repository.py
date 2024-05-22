from unittest.mock import patch, mock_open

import pytest

from app.domain.wine_trades.model.trades import TradeDataLog
from app.infrastructure import settings
from app.infrastructure.repositories.csv_wine_trades_repository import CSVTradeDataRepository

csv_data = """id;control;Produto;1970;1971
1;VINHO DE MESA;VINHO DE MESA;98327606;114399031
2;vm_Tinto;  Tinto;83300735;98327606;114399031
"""

settings.WINE_TRADE_FILE_PATH = "fake/path/to/wine_trades.csv"


@pytest.fixture
def mock_csv_file():
    with patch("builtins.open", mock_open(read_data=csv_data)):
        yield


def test_get_all_wine_trades_data(mock_csv_file):
    repository = CSVTradeDataRepository()
    result = repository.get_all_wine_trades_data()

    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].control == "VINHO DE MESA"
    assert len(result[0].tradeDataLogs) == 54  # From 1970 to 2023 (inclusive)
    assert result[0].tradeDataLogs[0] == TradeDataLog(year=1970, quantity="98327606")
    assert result[0].tradeDataLogs[1] == TradeDataLog(year=1971, quantity="114399031")
