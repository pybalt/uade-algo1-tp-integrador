from .directory import *
from .functions import *
import console.databases
import documents
from utils.json_handling import save_to_json


def handler(directory) -> str:
    console.databases.show_menu()
    user_input = input("Seleccione una opcion\n\t--> ").lower()

    if user_input == "a":
        console.databases.list_databases(directory)
    elif user_input == "b":
        database = access(directory)
        documents.handler(database)
    elif user_input == "c":
        name = input("Ingrese el nombre de la base de datos: ")
        create(name, directory)
    elif user_input == "exit()":
        console.exit(directory)  # Llama a la función exit que ahora guarda la base de datos

    return user_input