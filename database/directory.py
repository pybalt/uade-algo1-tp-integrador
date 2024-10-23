_directory = {}

def fill_directory():
    import json_handling
    global _directory
    _directory = json_handling.load_from_json()  # Cargar la base de datos desde JSON

def get_directory():
    return _directory 