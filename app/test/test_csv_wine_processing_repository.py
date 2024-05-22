from unittest.mock import patch, mock_open

import pytest

from app.domain.wine_processing.model.processing import ProcessingDataLog
from app.infrastructure import settings
from app.infrastructure.repositories.csv_wine_processing_repository import CSVProcessingDataRepository

csv_data = """id;control;cultivar;1970;1971
1;TINTAS;TINTAS;300;250
2;ti_Alicante Bouschet;Alicante Bouschet;300;250
"""

settings.WINE_PROCESSING_FILE_PATH = "fake/path/to/wine_processing.csv"


@pytest.fixture
def mock_csv_file():
    with patch("builtins.open", mock_open(read_data=csv_data)):
        yield


def test_get_all_wine_processing_data(mock_csv_file):
    repository = CSVProcessingDataRepository()
    result = repository.get_all_wine_processing_data()

    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].control == "TINTAS"
    assert result[0].cultivar == "TINTAS"
    assert len(result[0].processingDataLogs) == 54  # From 1970 to 2023 (inclusive)
    assert result[0].processingDataLogs[0] == ProcessingDataLog(year=1970, quantity="300")
    assert result[0].processingDataLogs[1] == ProcessingDataLog(year=1971, quantity="250")
