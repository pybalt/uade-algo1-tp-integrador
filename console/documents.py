def show_menu() -> None:
    """
    Prints the available choices to the console.
    Returns:
        None
    """
    print("Operaciones disponibles:")
    explanations = [
        ("1", "Crear documento"),
        ("2", "Listar documentos"),
        ("3", "Eliminar documento"),
        ("4", "Filtrar documentos por ID"),
        ("5", "Editar documento"),
        ("6",  "Buscar documento por patron"),
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
    limit = len(database)
    if limit == 0:
        print("No hay documentos en la base de datos.")
        return
    qty = int(input("De a cuantos documentos desea ver: "))

    for i in range(0, limit, qty):
        print(f"Mostrando documentos {i+1} a {min(i + qty, limit)}:")

        for index, key in enumerate(list(database.keys())[i : i + qty], start=i + 1):
            print(f"{index}. \"{''.join(key)}\": {database[key]}")

        if i + qty < limit:
            user_input = input("Deseas ver más documentos? (s/n): ")
            user_want_to_terminate = user_input.lower() != "s"
            if user_want_to_terminate:
                break
        else:
            print("No hay más documentos para mostrar.")
