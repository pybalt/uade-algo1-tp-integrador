import uuid
import re
from utils import parse_value

def select_distinct(database: dict) -> None:
    unique_documents = set()

    for _, doc_data in database.items():
        doc_str = str(doc_data)
        unique_documents.add(doc_str)

    print("Documentos únicos en la base de datos:")
    for unique_doc in unique_documents:
        print(unique_doc)


def search_by_regex(database: dict) -> None:
    """
    Search for documents in the database that contain a value matching the regular expression.
    Args:
        database (dict): The database where to search for documents.
    """
    regex_pattern = input("Enter the regular expression to search for: ")
    regex = re.compile(regex_pattern)
    matches = False

    found_matches = filter(
        lambda x: any(regex.search(str(value)) or regex.search(str(key))
                     for key, value in x[1].items()),
        database.items()
    )

    for doc_id, document in list(found_matches):
        print(f"Document found with ID: {str(doc_id)}")
        print(f"Document data: {document}\n")
        matches = True

    if not matches:
        print("No matches found for the entered pattern.")


def create(database: dict) -> None:
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

    document_id = uuid.uuid4()
    document_data = {}

    print("Creando un nuevo documento...")
    print(
        "Los tipos de datos soportados son: string, int, float, tuple, list, set, matrix"
    )
    print("El formato de entrada es 'tipo.valor1,valor2,...'")
    print(
        "Para los tipos de datos tales como set, tuple, list y matrix, separe los valores con comas."
    )
    print(
        "Ademas, para los tipos de datos como matrix, separe las filas con punto y coma."
    )

    field_name = input("Ingrese el nombre del campo (o 'exit()' para terminar): ")
    while field_name.lower() != "exit()":
        field_value = input(f"Ingrese el valor para el campo '{field_name}': ")
        parsed_value = parse_value(field_value)
        document_data[field_name] = parsed_value

        field_name = input("Ingrese el nombre del campo (o 'exit()' para terminar): ")

    database[document_id] = document_data

    print(f"\nDocumento creado con ID: {document_id}")
    print(f"Datos del documento: {document_data}\n")


def edit(database: dict) -> None:
    id = uuid.UUID(input("Introducir el id del documento: "))
    if id in database:
        print(id, database[id])
        field_name = input("Introducir el nombre del campo a editar: ")
        field_value = input("Introducir el valor del campo: ")
        parsed_value = parse_value(field_value)
        database[id][field_name] = parsed_value
    else:
        print(f"No se encontró ningún documento con el ID: {id}")

def delete(database: dict) -> None:
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
    document_id = uuid.UUID(input("Ingrese el ID del documento a eliminar: "))
    if document_id in database:
        del database[document_id]
        print(f"Documento con ID: {document_id} eliminado exitosamente.")
    else:
        print(f"No se encontró ningún documento con el ID: {document_id}")


def filter_by_id(database: dict) -> None:
    """
    Filters and prints a document from the database based on user input ID.
    Args:
        database (dict): A dictionary where keys are document IDs (tuples) and values are document details.
    Returns:
        None
    The function prompts the user to input a document ID, filters the document from the database,
    and prints the document details if found. If no document is found with the given ID, it prints
    an appropriate message.
    """

    id = uuid.UUID(input("Introducir el id del documento: "))

    if id in database:
        doc = database[id]
        print(id, doc)
    else:
        print(f"No se encontró ningún documento con el ID: {id}")