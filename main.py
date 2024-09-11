def get_databases() -> dict:
    """
    Retrieves a list of databases.

    Returns:
        list: A list of databases.
    """
    databases = {"pepe": {}}
    return databases


def create_database(name: str, directory):
    """
    Creates a new database with the given name.

    Parameters:
    - name (str): The name of the database.
    - directory: The directory where the database will be stored.
    """
    databases[name] = {}


def list_databases(directory) -> None:
    """
    Prints the names of the databases in the given directory.

    Parameters:
    - directory: Where databases are stored.

    Returns:
    None
    """
    for db in directory:
        print(db)


def access_database(directory): 
    """
    Accesses a database in the given directory.

    Parameters:
    directory (dict): A dictionary containing the databases.

    Returns:
    Any: The database corresponding to the given name.

    Raises:
    KeyError: If the database does not exist.

    """
    database_name = input("Ingrese nombre de base de datos.\n\t--> ")
    print(f"Accediendo a la base de datos {database_name}")
    return directory[database_name]

def exit():
    print("Saliendo del programa...")

def get_choices() -> dict:
    """
    Returns a dictionary of choices.

    Returns:
        dict: A dictionary containing the choices.
    """
    choices = {"a": list_databases, "b": access_database, "exit()": exit}
    return choices


def list_choices(choices: dict) -> None:
    print("Sus opciones son")
    explanations = [
        ("A", "Listar bases de datos"),
        ("B", "Acceder directamente a una base de datos"),
        ("exit()", "Salir del programa"),
    ]
    
    assert len(explanations) == len(choices) # For development purposes. Delete before sprint 1.

    for key, value in explanations:
        print(f"\t{key}: {value}")


def handle_options(choices) -> str:

    list_choices(choices)
    user_input = input("Seleccione una opcion\n\t--> ")

    if user_input.lower() in choices:
        choices[user_input.lower()](databases)

    return user_input


if __name__ == "__main__":
    """
    El codigo debajo de este if, es el que define
    la interaccion con el usuario
    """

    print("Bienvenidos a la base de datos no relacional de Base Builders!")
    print("Para continuar, presione una tecla")
    user_input = input("")
    choices = get_choices()
    while user_input != "exit()":

        databases = get_databases()
        if not databases:
            print("No se han creado bases de datos.")
            database_name = input("Ingrese nombre de base de datos.\n\t--> ")
            create_database(database_name, databases)

        user_input = handle_options(choices)
