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
        database = access(directory)
        documents.handler(database)
    elif user_input == "c":
        name = input("Ingrese el nombre de la base de datos: ")
        create(name, directory)
    elif user_input == "exit()":
        console.exit()

    return user_input
