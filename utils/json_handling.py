import json

def save_to_json(directory: dict, filename: str = "database.json") -> None:
    try:
        with open(filename, "w") as json_file:
            json.dump(directory, json_file)
        print(f"Base de datos guardada en {filename}")
    except IOError as e:
        print(f"Error al guardar la base de datos: {e}")

def load_from_json(filename: str = "database.json") -> dict:
    try:
        with open(filename, "r") as json_file:
            return json.load(json_file)
    except (IOError, json.JSONDecodeError):
        print(f"No se pudo cargar la base de datos desde {filename}. Creando una nueva.")
        return {}