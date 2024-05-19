class ExportLog:
    def __init__(self, export_log_dict):
        self.year = export_log_dict['year']
        self.quantity = export_log_dict['quantity']
        self.price = export_log_dict['price']


class ExportData:
    def __init__(self, id_value, country, export_logs):
        self.id = id_value
        self.country = country
        self.export_logs = [ExportLog(export_log) for export_log in export_logs]
