from database import *
import console.databases
import documents

def start():
    try:
        user_input = input("")
        directory = get_directory()
        fill(directory)
        while user_input != "exit()":
            if not directory:
                print("No se han creado bases de datos.")
                database_name = input("Ingrese nombre de base de datos.\n\t--> ")
                create(database_name, directory)

            user_input = handler(directory)
    except KeyboardInterrupt:
        print("\nGracias por usar Base Builders!")
    finally:
        update_dictory()