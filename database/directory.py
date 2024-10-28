from utils.json_handling import load_from_json

def initialize_directory():
    """
    Inicializa el directorio cargándolo desde un archivo JSON.
    """
    directory = load_from_json()  
    return directory

def get_directory(directory):
    """
    Devuelve el contenido actual del directorio.
    
    Args:
        directory (dict): El directorio a devolver.
    """
    return directory