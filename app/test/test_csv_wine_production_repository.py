from unittest.mock import patch, mock_open

import pytest

from app.domain.wine_production.model.production import ProductionLog
from app.infrastructure import settings
from app.infrastructure.repositories.csv_wine_production_repository import CSVProductionDataRepository

csv_data = """id;produto;1970;1971
1;VINHO DE MESA;217208604;154264651
2;Tinto;174224052;121133369
"""


settings.WINE_PRODUCTION_DATA_FILE_PATH = "fake/path/to/wine_production.csv"


@pytest.fixture
def mock_csv_file():
    with patch("builtins.open", mock_open(read_data=csv_data)):
        yield


def test_get_all_wine_production_data(mock_csv_file):
    repository = CSVProductionDataRepository()
    result = repository.get_all_wine_production_data()

    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].product == "VINHO DE MESA"
    assert len(result[0].productionLogs) == 54  # From 1970 to 2023 (inclusive)
    assert result[0].productionLogs[0] == ProductionLog(year=1970, quantity="217208604")
    assert result[0].productionLogs[1] == ProductionLog(year=1971, quantity="154264651")
