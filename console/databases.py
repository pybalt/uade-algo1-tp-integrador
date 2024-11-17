import pprint
import console

def list_databases(directory: dict) -> None:
    """

    Prints the names of the databases in the given directory.


    Parameters:

    - directory: Where databases are stored.


    Returns:

    None
    """

    for key, db in enumerate(directory):

        print(key + 1, db)


def show_menu() -> None:
    """

    Prints the available choices to the console.

    Args:

        choices (dict): A dictionary containing the available choices.

    Returns:

        None
    """

    console.log("Sus opciones son")

    explanations = [
        ("A", "Listar bases de datos"),
        ("B", "Acceder directamente a una base de datos"),
        ("C", "Crear una nueva base de datos"),
        ("D", "Unir dos bases de datos"),
        ("E", "Intersección de dos bases de datos"),
        ("F", "Diferencia de dos bases de datos"),
        ("G", "Diferencia simétrica de dos bases de datos"),
        ("exit()", "Salir del programa"),
    ]

    for key, value in explanations:
        console.log(f"\t{key}: {value}")

def show_set_operation(dataset: dict) -> None:
    """
    Prints the result of the set operation.
    """
    console.log("El resultado de la operación es:")
    for dict in dataset:
        pprint.pprint(dict)
