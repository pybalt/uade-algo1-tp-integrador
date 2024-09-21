import uuid

directory = {}

def create_database(name: str, directory):
    """
    Creates a new database with the given name.

    Parameters:
    - name (str): The name of the database.
    - directory: The directory where the database will be stored.
    """
    directory[name] = {}

def create_document(database: dict) -> None:
    """
    Crea un nuevo documento en la base de datos con un ID único y almacena los campos
    como tuplas.

    Parameters:
    - database (dict): La base de datos en la que se almacenará el documento.
    
    Returns:
    None
    """

    document_id = str(uuid.uuid4())
    document_data = {}
    
    while True:
        field_name = input("Ingrese el nombre del campo (o 'exit()' para terminar): ")
        if field_name.lower() == 'exit()':
            break
        field_value = input(f"Ingrese el valor para el campo '{field_name}': ")
        
        document_data[field_name] = field_value

    # Almacenar el documento en la base de datos
    database[tuple(document_id)] = document_data
    
    print(f"\nDocumento creado con ID: {document_id}")
    print(f"Datos del documento: {document_data}\n")

def list_databases(directory) -> None:
    """
    Prints the names of the databases in the given directory.

    Parameters:
    - directory: Where databases are stored.

    Returns:
    None
    """
    for key, db in enumerate(directory):
        print(key+1, db)


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


def list_choices() -> None:
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

def list_database_choices() -> None:
    """
    Prints the available choices to the console.
    Args:
        choices (dict): A dictionary containing the available choices.
    Returns:
        None
    """
    print("Operaciones disponibles:")
    explanations = [
        ("1", "Crear documento"),
        ("exit()", "Volver al menú principal"),
    ]

    for key, value in explanations:
        print(f"\t{key}: {value}")

def handle_database_operations(database: dict) -> None:
    """
    Provides options to operate within the selected database.

    Parameters:
    - database (dict): The current database being operated on.

    Returns:
    None
    """
    list_database_choices()
    option = input("Seleccione una opción:\n\t--> ")
    while option != "exit()":

        if option == "1":
            create_document(database)

        list_database_choices()
        option = input("Seleccione una opción:\n\t--> ")

def handle_options() -> str:
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
    list_choices()
    user_input = input("Seleccione una opcion\n\t--> ").lower()

    if user_input == "a":
        list_databases(directory)
    elif user_input == "b":
        database = access_database(directory)
        handle_database_operations(database)
    elif user_input == "c":
        name = input("Ingrese el nombre de la base de datos: ")
        create_database(name, directory)
    elif user_input == "exit()":
        exit()

    return user_input


if __name__ == "__main__":
    """
    The code below this if statement defines the interaction with the user.
    """

    print("Bienvenidos a la base de datos no relacional de Base Builders!")
    print("Para continuar, presione una tecla")
    user_input = input("")

    while user_input != "exit()":

        if not directory:
            print("No se han creado bases de datos.")
            database_name = input("Ingrese nombre de base de datos.\n\t--> ")
            create_database(database_name, directory)

        user_input = handle_options()
