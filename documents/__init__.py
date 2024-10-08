from .functions import *
import console.documents


def handler(database: dict) -> None:
    """
    Provides options to operate within the selected database.

    Parameters:
    - database (dict): The current database being operated on.

    Returns:
    None
    """
    console.documents.show_menu()
    option = input("Seleccione una opción:\n\t--> ")
    while option != "exit()":

        if option == "1":
            create(database)
        elif option == "2":
            console.documents.list_documents(database)
        elif option == "3":
            delete_document(database)
        elif option == "4":
            filter_by_id(database)
        elif option == "5":
            edit(database)

        console.documents.show_menu()
        option = input("Seleccione una opción:\n\t--> ")
