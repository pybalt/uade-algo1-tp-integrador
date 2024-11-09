from database import *

def start():
    user_input = input("")
    directory = get_directory()
    fill(directory)
    while user_input != "exit()":
        if not directory:
            print("No se han creado bases de datos.")
            database_name = input("Ingrese nombre de base de datos.\n\t--> ")
            create(database_name, directory)

        user_input = handler(directory)