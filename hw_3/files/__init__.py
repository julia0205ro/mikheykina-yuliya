import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


USER_JSON_FILE_PATH = get_path(filename='user.json')
BOOKS_CSV_FILE_PATH = get_path(filename='books.csv')
REFERENCE_JSON_FILE_PATH = get_path(filename='reference.json')
