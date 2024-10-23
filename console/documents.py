def list_documents(database: dict) -> None:
    """
    Lists documents from the provided database in chunks specified by the user, unless there is only one document.
    Args:
        database (dict): A dictionary where keys are document identifiers and values are document contents.
    """
    limit = len(database)
    if limit == 0:
        print("No hay documentos en la base de datos.")
        return
    elif limit == 1:
        key = list(database.keys())[0]
        print(f"1. \"{key}\": {database[key]}")
        return

    while True:
        qty_input = input("De a cuántos documentos desea ver: ")
        
        if not qty_input.strip(): 
            print("Error: La entrada no puede estar vacía. Por favor, ingresa un número válido.")
            continue

        try:
            qty = int(qty_input)
            if qty <= 0:  
                print("Error: Debes ingresar un número positivo.")
                continue
            break 

        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

    for i in range(0, limit, qty):
        print(f"Mostrando documentos {i + 1} a {min(i + qty, limit)}:")

        for index, key in enumerate(list(database.keys())[i: i + qty], start=i + 1):
            print(f"{index}. \"{key}\": {database[key]}")

        if i + qty < limit:
            user_input = input("¿Deseas ver más documentos? (s/n): ")
            user_want_to_terminate = user_input.lower() != "s"
            if user_want_to_terminate:
                break
        else:
            print("No hay más documentos para mostrar.")