from unittest.mock import patch, mock_open

import pytest

from app.domain.wine_imports.model.imports import ImportLog
from app.infrastructure import settings
from app.infrastructure.repositories.csv_wine_imports_repository import CSVImportDataRepository

csv_data = """Id;País;1970_q;1970_v;1971_q;1971_v
1;Country1;100;200;150;250
2;Country2;200;300;250;350
"""

settings.WINE_IMPORT_FILE_PATH = "fake/path/to/wine_imports.csv"


@pytest.fixture
def mock_csv_file():
    with patch("builtins.open", mock_open(read_data=csv_data)):
        yield


def test_get_all_wine_imports_data(mock_csv_file):
    repository = CSVImportDataRepository()
    result = repository.get_all_wine_imports_data()

    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].country == "Country1"
    assert len(result[0].import_logs) == 54  # From 1970 to 2023 (inclusive)
    assert result[0].import_logs[0] == ImportLog(year=1970, quantity="100", price="200")
    assert result[0].import_logs[1] == ImportLog(year=1971, quantity="150", price="250")
