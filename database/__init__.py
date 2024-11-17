from .directory import *
from .functions import *
import console.databases
import documents


def handler(directory) -> str:
    console.databases.show_menu()
    user_input = input("Seleccione una opcion\n\t--> ").lower()

    # TODO: Reformat this function to use the console module. database.__init__.handler
    # TODO: Reformat try-except blocks to use console.error and console.log. database.__init__.handler
    try:
        if user_input == "a":
            console.databases.list_databases(directory)
        elif user_input == "b":
            database, database_name = access(directory)
            documents.handler(database)
        elif user_input == "c":
            name = input("Ingrese el nombre de la base de datos: ")
            create(name, directory)
            console.log(f"Base de datos {name} creada exitosamente.")
        elif user_input == "d":
            database1, _ = access(directory)
            database2, _ = access(directory)
            console.databases.show_set_operation(union(database1, database2))
        elif user_input == "e":
            database1, _ = access(directory)
            database2, _ = access(directory)
            console.databases.show_set_operation(intersection(database1, database2))
        elif user_input == "f":
            database1, _ = access(directory)
            database2, _ = access(directory)
            console.databases.show_set_operation(difference(database1, database2))
        elif user_input == "g":
            database1, _ = access(directory)
            database2, _ = access(directory)
            console.databases.show_set_operation(symmetric_difference(database1, database2))
        elif user_input == "exit()":
            console.exit()
    except AssertionError as e:
        console.error(e)
    except KeyboardInterrupt:
        pass
    finally:
        if 'database' in locals() and 'database_name' in locals():
            save(database, database_name, directory)
            console.log(f"Base de datos {database_name} guardada exitosamente.")
            update_dictory()
    return user_input