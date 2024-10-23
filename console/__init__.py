from utils.json_handling import save_to_json

def exit(directory: dict) -> None:
    save_to_json(directory)  # Guardar la base de datos antes de salir
    print("Saliendo del programa...") 