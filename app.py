from typing import Callable
import database
import console


def start():
    user_input = input("")
    directory = database.get_directory()
    while user_input != "exit()":

        if not directory:
            print("No se han creado bases de datos.")
            database_name = input("Ingrese nombre de base de datos.\n\t--> ")
            database.create(database_name, directory)

        user_input = database.handler(directory)
