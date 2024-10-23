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

    print("Sus opciones son")

    explanations = [
        ("A", "Listar bases de datos"),
        ("B", "Acceder directamente a una base de datos"),
        ("C", "Crear una nueva base de datos"),
        ("exit()", "Salir del programa"),
    ]

    for key, value in explanations:

        print(f"\t{key}: {value}")