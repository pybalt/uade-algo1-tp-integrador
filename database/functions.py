def create(name: str, directory):
    """
    Creates a new database with the given name.

    Parameters:
    - name (str): The name of the database.
    - directory: The directory where the database will be stored.

    Returns:
    None

    Example:
    >>> create("mi_base_datos", directory)
    """
    directory[name] = {}


def access(directory: dict):
    """
    Accesses a database in the given directory.

    Parameters:
    directory (dict): A dictionary containing the databases.

    Returns:
    dict: The database corresponding to the given name.

    Raises:
    KeyError: If the database does not exist.

    Example:
    >>> db = access(directory)
    Ingrese nombre de base de datos.
        --> mi_base_datos
    Accediendo a la base de datos mi_base_datos
    """
    database_name = input("Ingrese nombre de base de datos.\n\t--> ")
    print(f"Accediendo a la base de datos {database_name}")
    return directory[database_name]


def hashable_value(value):
    if isinstance(value, dict):
        return frozenset((k, hashable_value(v)) for k, v in value.items())
    elif isinstance(value, list):
        return tuple(hashable_value(v) for v in value)
    return value

def frozenset_to_readable(fset):
    def unpack(value):
        if isinstance(value, frozenset):
            return {k: unpack(v) for k, v in value}
        elif isinstance(value, list):
            return [unpack(v) for v in value]
        return value

    return {k: unpack(v) for k, v in fset}


def union(database1: dict, database2: dict):
    result = set(hashable_value(v) for v in database1.values()) | set(hashable_value(v) for v in database2.values())
    return [frozenset_to_readable(f) for f in result]

def intersection(database1: dict, database2: dict):
    result = set(hashable_value(v) for v in database1.values()) & set(hashable_value(v) for v in database2.values())
    return [frozenset_to_readable(f) for f in result]

def difference(database1: dict, database2: dict):
    result = set(hashable_value(v) for v in database1.values()) - set(hashable_value(v) for v in database2.values())
    return [frozenset_to_readable(f) for f in result]

def symmetric_difference(database1: dict, database2: dict):
    result = set(hashable_value(v) for v in database1.values()) ^ set(hashable_value(v) for v in database2.values())
    return [frozenset_to_readable(f) for f in result]

