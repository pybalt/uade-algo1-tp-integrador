from .directory import *
from .functions import *
import console.databases
import documents


def handler(directory) -> str:
    """
    Handles the user's options and returns the selected option.
    Parameters:
    - choices (dict): A dictionary containing the available choices and their corresponding functions.
    Returns:
    - str: The selected option.
    Example:
    >>> handle_options({'a': function_a, 'b': function_b})
        a: Explanation A
        b: Explanation B
        Select an option
            --> a
        ---
        function_a() will be executed.
    """
    console.databases.show_menu()
    user_input = input("Seleccione una opcion\n\t--> ").lower()
    if user_input == "a":
        console.databases.list_databases(directory)
    elif user_input == "b":
        try:
            database = access(directory)
            documents.handler(database)
        except KeyError:
            print(f'La base de datos no existe.')
    elif user_input == "c":
        name = input("Ingrese el nombre de la base de datos: ")
        try:
            create(name, directory)
        except KeyError:
            print(f'La base de datos {name} no existe.')
    elif user_input == "d":
        database1 = access(directory)
        database2 = access(directory)
        console.databases.show_set_operation(union(database1, database2))
    elif user_input == "e":
        database1 = access(directory)
        database2 = access(directory)
        console.databases.show_set_operation(intersection(database1, database2))
    elif user_input == "f":
        database1 = access(directory)
        database2 = access(directory)
        console.databases.show_set_operation(difference(database1, database2))
    elif user_input == "g":
        database1 = access(directory)
        database2 = access(directory)
        console.databases.show_set_operation(symmetric_difference(database1, database2))
    elif user_input == "exit()":
        console.exit()

    return user_input