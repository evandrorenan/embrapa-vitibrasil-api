import os


def normalized_path(file):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir_data = os.path.join(base_dir, 'data', file)
    return os.path.normpath(base_dir_data)

class Settings:
    WINE_EXPORT_FILE_PATH = normalized_path('ExpVinho.csv')



settings = Settings()
