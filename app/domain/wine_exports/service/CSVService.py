import csv

from itertools import groupby
from operator import itemgetter
from typing import List

from app.core.settings import settings
from app.domain.wine_exports.model.exports import ExportData


class CSVService:
    @staticmethod
    def read_csv() -> List[ExportData]:
        with open(settings.EXPORT_FILE_PATH, mode='r') as file:
            csv_reader = csv.DictReader(file)
            rows = list(csv_reader)

        key_func = itemgetter('id', 'country')
        rows.sort(key=key_func)

        grouped_data = {
            (key[0], key[1]): list(group)
            for key, group in groupby(rows, key=key_func)
        }

        export_data_list = [
            ExportData(
                id_value=id_value,
                country=country,
                export_logs=[
                    {'year': row['year'], 'quantity': row['quantity'], 'price': row['price']}
                    for row in group
                ]
            )
            for (id_value, country), group in grouped_data.items()
        ]

        return export_data_list

