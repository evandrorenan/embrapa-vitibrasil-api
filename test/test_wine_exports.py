from decimal import Decimal
import pytest
from fastapi.testclient import TestClient
from app.di.dependencies import get_service
from app.domain.wine_exports.model.exports import ExportData, ExportLog
from app.domain.wine_exports.service.core import WineExportService
from app.main import app


class MockWineExportService(WineExportService):
    def list_all(self):
        return [
            ExportData(id=1, country="Brazil", export_logs=[ExportLog(year=2022, quantity=Decimal("20"), price="200")]),
            ExportData(id=2, country="France", export_logs=[ExportLog(year=2022, quantity=Decimal("10"), price="100")])
        ]


class FailingMockWineExportService(WineExportService):
    def list_all(self):
        raise Exception("Database connection error")


def get_mock_service():
    return MockWineExportService()


def get_failing_mock_service():
    return FailingMockWineExportService()


@pytest.fixture
def client():
    app.dependency_overrides[get_service] = get_mock_service
    with TestClient(app) as c:
        yield c
    app.dependency_overrides = {}


@pytest.fixture
def failing_client():
    app.dependency_overrides[get_service] = get_failing_mock_service
    with TestClient(app) as c:
        yield c
    app.dependency_overrides = {}


def test_get_wine_exports_data_success(client):
    response = client.get("api/v1/wine-exports")
    print (response.json())
    assert response.status_code == 200
    assert response.json() == [
        {'id': 1, 'country': 'Brazil', 'export_logs': [
            {'year': 2022, 'quantity': '20', 'price': '200'}
        ]},
        {'id': 2, 'country': 'France', 'export_logs': [
            {'year': 2022, 'quantity': '10', 'price': '100'}
        ]}
    ]


def test_get_wine_exports_data_failure(failing_client):
    response = failing_client.get("api/v1/wine-exports")
    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}
