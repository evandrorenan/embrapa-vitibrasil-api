import os


class Settings:
    print(os.path.join(os.path.dirname(__file__)))
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    EXPORT_FILE_PATH = os.path.join(BASE_DIR, 'data', 'ExpVinho.csv')
    EXPORT_FILE_PATH = os.path.normpath(EXPORT_FILE_PATH)


settings = Settings()
