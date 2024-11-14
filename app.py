from database import *
import console
import console.databases
import console

def start():
    try:
        user_input = ""
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
        exit()
    finally:
        console.log("\nGracias por usar Base Builders!")
        if 'directory' in locals() and directory.keys():
            update_dictory()