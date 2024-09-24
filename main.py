from locale import dcgettext
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
    Creates a new document with user-provided fields and values, and stores it in the given database.
    Args:
        database (dict): The database where the new document will be stored. The database is expected to be a dictionary.
    The function generates a unique document ID using UUID, prompts the user to input field names and values,
    and stores the document in the database with the generated ID as the key. The user can exit the input loop
    by typing 'exit()' as the field name.
    Example:
        database = {}
        create_document(database)
        # User inputs field names and values
        # Document is stored in the database with a unique ID
    """


    document_id = str(uuid.uuid4())
    document_data = {}
    
    while True:
        field_name = input("Ingrese el nombre del campo (o 'exit()' para terminar): ")
        if field_name.lower() == 'exit()':
            break
        field_value = input(f"Ingrese el valor para el campo '{field_name}': ")
        
        document_data[field_name] = field_value

    database[tuple(document_id)] = document_data
    
    print(f"\nDocumento creado con ID: {document_id}")
    print(f"Datos del documento: {document_data}\n")

def delete_document(database: dict) -> None:
    """
    Deletes a document from the database based on the provided document ID.

    Args:
        database (dict): The database from which the document will be deleted. 
                         The keys are document IDs and the values are the document data.

    Returns:
        None

    Prompts the user to input the ID of the document to delete. If the document ID exists in the database,
    it deletes the document and prints a success message. If the document ID does not exist, it prints an error message.
    """
    document_id= input("Ingrese el ID del documento a eliminar: ")
    if document_id in database:
        del database[document_id]
        print(f"Documento con ID: {document_id} eliminado exitosamente.")
    else:
        print(f"No se encontró ningún documento con el ID: {document_id}")

def list_databases(directory: dict) -> None:
    """
    Prints the names of the databases in the given directory.

    Parameters:
    - directory: Where databases are stored.

    Returns:
    None
    """
    for key, db in enumerate(directory):
        print(key+1, db)


def access_database(directory: dict):
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
        ("2", "Listar documentos"),
        ("exit()", "Volver al menú principal"),
    ]

    for key, value in explanations:
        print(f"\t{key}: {value}")

def list_documents(database: dict) -> None:
    """
    Lists documents from the provided database in chunks specified by the user.
    Args:
        database (dict): A dictionary where keys are document identifiers and values are document contents.
    The function prompts the user to input the number of documents they wish to view at a time.
    It then displays the documents in chunks, allowing the user to decide whether to continue viewing more documents.
    User Inputs:
        - Number of documents to view at a time.
        - Whether to continue viewing more documents after each chunk.
    Example:
        database = {
            'doc1': 'Content of document 1',
            'doc2': 'Content of document 2',
            'doc3': 'Content of document 3',
            ...
        }
        list_documents(database)
    """
    qty = int(input("De a cuantos documentos desea ver: "))
    limit = len(database)

    for i in range(0, limit, qty):
        print(f"Mostrando documentos {i+1} a {min(i + qty, limit)}:")

        for index, key in enumerate(list(database.keys())[i:i + qty], start=i + 1):
            print(f"{index}. {database[key]}")

        user_input = input("Deseas ver más documentos? (s/n): ")
        user_want_to_terminate = user_input.lower() != "s"
        if user_want_to_terminate:
            break


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
        if option == "2":
            list_documents(database)

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

def filter_documents_by_id(document_collection: dict) -> None:
    """
    Filtra una lista de documentos por su ID y muestra el documento filtrado.
    Args:
        documentos (list): Lista de diccionarios, donde cada diccionario representa un documento
                           con las claves "id" y "contenido".
    Returns:
        None: Esta función no retorna ningún valor. Imprime el documento filtrado o un mensaje
              indicando que no se encontró ningún documento con el ID proporcionado.
    """

    id = input("Introducir el id del documento: ")
    filtered_documents = [doc for doc in document_collection if doc["id"] == id]

    if filtered_documents:
        print({"id": filtered_documents[0]["id"], "contenido": filtered_documents[0]["contenido"]})
    else:
        print(f"No se encontró ningún documento con el ID: {id}")



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
