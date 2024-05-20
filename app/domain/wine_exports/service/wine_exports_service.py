class WineExportService:
    def __init__(self, export_data_repository: ExportDataRepository):
        self.export_data_repository = export_data_repository

    def list_all(self) -> List[ExportData]:
        return self.export_data_repository.get_export_data()


class WineExportsRepository:
    def get_all_wine_exports_data(self) -> List[ExportData]:
        pass
