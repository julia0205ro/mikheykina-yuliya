import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


DOG_BREEDS_JSON_FILE_PATH = get_path(filename='dog_breeds.json')
