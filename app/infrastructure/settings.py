import os


def normalized_path(file):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir_data = os.path.join(base_dir, 'data', file)
    return os.path.normpath(base_dir_data)


WINE_PRODUCTION_DATA_FILE_PATH = normalized_path('Producao.csv')
WINE_PROCESSING_DATA_FILE_PATH = normalized_path('ProcessaViniferas.csv')
WINE_TRADES_FILE_PATH = normalized_path('Comercio.csv')
WINE_IMPORTS_DATA_FILE_PATH = normalized_path('ImpVinhos.csv')
WINE_EXPORT_FILE_PATH = normalized_path('ExpVinho.csv')
