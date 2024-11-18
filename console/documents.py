import console

def show_menu(database_name: str) -> None:
    """
    Prints the available choices to the console.
    Returns:
        None
    """

    explanations = [
        ("1", "Crear documento"),
        ("2", "Listar documentos"),
        ("3", "Eliminar documento"),
        ("4", "Filtrar documentos por ID"),
        ("5", "Editar documento"),
        ("6", "Buscar documento por patron"),
        ("7", "Mostrar documentos unicos"),
        ("exit()", "Volver al menú principal"),
    ]
    option, title = console.show_options_menu(explanations, f"Base de datos: {database_name}")
    return option

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
    assert limit > 0, "No hay documentos en la base de datos."
    
    while True:
        qty_input = input("De a cuántos documentos desea ver: ")
        
        if not qty_input.strip(): 
            console.error("Error: La entrada no puede estar vacía. Por favor, ingresa un número válido.")
            continue

        try:
            qty = int(qty_input)
            if qty <= 0:  
                console.error("Error: Debes ingresar un número positivo.")
                continue
            break 

        except ValueError:
            console.error("Error: Por favor, ingresa un número válido.")

    for i in range(0, limit, qty):
        console.log(f"Mostrando documentos {i + 1} a {min(i + qty, limit)}:")

        for index, key in enumerate(list(database.keys())[i: i + qty], start=i + 1):
            console.log(f"{index}. \"{key}\": {database[key]}")

        if i + qty < limit:
            user_input = input("¿Deseas ver más documentos? (s/n): ")
            user_want_to_terminate = user_input.lower() != "s"
            if user_want_to_terminate:
                break
        else:
            console.log("No hay más documentos para mostrar.")
