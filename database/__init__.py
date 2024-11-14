from .directory import *
from .functions import *
import console.databases
import documents


def handler(directory) -> str:
    user_input = console.databases.show_menu()
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
        console.pause_program()
        return user_input
    except AssertionError as e:
        console.error(e)
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except SystemExit:
        raise SystemExit
    finally:
        if 'database' in locals() and 'database_name' in locals():
            save(database, database_name, directory)
            console.log(f"Base de datos {database_name} guardada exitosamente.")
            update_dictory()