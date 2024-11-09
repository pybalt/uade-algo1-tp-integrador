import os
import json

_directory = {}
DIRECTORY_FILE = "data/directory.json"


def fill(directory_dict: dict):
    os.makedirs(os.path.dirname(DIRECTORY_FILE), exist_ok=True)
    if os.path.exists(DIRECTORY_FILE):
        with open(DIRECTORY_FILE, "r") as f:
            _directory = json.load(f)
            directory_dict.update(_directory)
    else:
        update_dictory()

def update_dictory():
    with open(DIRECTORY_FILE, "w") as f:
        json.dump(_directory, f)

def get_directory():
    """
    Devuelve el contenido actual del directorio.
    
    Args:
        directory (dict): El directorio a devolver.
    """
    return _directory