import pytest
from unittest.mock import patch, mock_open
from app.domain.wine_exports.model.exports import ExportLog
from app.infrastructure.csv_wine_exports_repository import CSVExportDataRepository
from app.infrastructure.settings import settings

csv_data = """Id;País;1970_q;1970_v;1971_q;1971_v
1;Country1;100;200;150;250
2;Country2;200;300;250;350
"""

settings.WINE_EXPORT_FILE_PATH = "fake/path/to/wine_exports.csv"

@pytest.fixture
def mock_csv_file():
    with patch("builtins.open", mock_open(read_data=csv_data)):
        yield

def test_get_all_wine_exports_data(mock_csv_file):
    repository = CSVExportDataRepository()
    result = repository.get_all_wine_exports_data()

    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].country == "Country1"
    assert len(result[0].export_logs) == 54  # From 1970 to 2023 (inclusive)
    assert result[0].export_logs[0] == ExportLog(year=1970, quantity="100", price="200")
    assert result[0].export_logs[1] == ExportLog(year=1971, quantity="150", price="250")
