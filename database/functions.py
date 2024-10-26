def create(name: str, directory):
    """
    Creates a new database with the given name.

    Parameters:
    - name (str): The name of the database.
    - directory: The directory where the database will be stored.
    """
    directory[name] = {}


def access(directory: dict):
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
    try:
        print(f"Accediendo a la base de datos {database_name}")
        return directory[database_name]
    except KeyError:
        print(f"La base de datos llamada {database_name} no existe")
        return None