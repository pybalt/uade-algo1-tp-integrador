from database import *
import console
import console.databases


def start():
    try:
        user_input = input("")
        directory = get_directory()
        fill(directory)
        while user_input != "exit()":
            if not directory:
                console.log("No se han creado bases de datos.")
                database_name = input("Ingrese nombre de base de datos.\n\t--> ")
                create(database_name, directory)
                console.log(f"Base de datos {database_name} creada exitosamente.")

            user_input = handler(directory)
    except KeyboardInterrupt:
        console.log("\nGracias por usar Base Builders!")
    finally:
        update_dictory()