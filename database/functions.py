import json, os, uuid
from functools import reduce

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
    assert name not in directory, f"La base de datos {name} ya existe."
    directory[name] = f'data/{name}.json'
    with open(directory[name], 'w') as f:
        json.dump({}, f, indent=4)
    print(f"Base de datos {name} creada exitosamente.")

def str_to_uuid(data: dict):
    new_dict = {}
    for key, value in data.items():
        if isinstance(key, str) and key.startswith("UUID("):
            new_key = uuid.UUID(key[5:-1])
            new_dict[new_key] = value
        else:
            new_dict[key] = value
    return new_dict

def uuid_to_str(data: dict):
    new_dict = {}
    for key, value in data.items():
        if isinstance(key, uuid.UUID):
            new_key = f"UUID({key})"
            new_dict[new_key] = value
        else:
            new_dict[key] = value
    return new_dict

def save(content: dict, database_name: str, directory: dict):
    file_path = directory[database_name]
    content = uuid_to_str(content)
    with open(file_path, 'w') as f:
        json.dump(content, f, indent=4)
    print(f"Base de datos {database_name} guardada exitosamente.")

def delete(database_name: str, directory: dict):
    if database_name not in directory:
        print(f"La base de datos {database_name} no existe.")
        return
    file_path = directory[database_name]
    try:
        os.remove(file_path)
        del directory[database_name]
        save(directory, "directory", directory)
        print(f"Base de datos {database_name} eliminada exitosamente.")
    except Exception as e:
        print(f"Error al eliminar la base de datos {database_name}: {e}")

def access(directory: dict) -> tuple[dict, str]:
    """
    Accesses a database in the given directory.

    This function prompts the user to enter the name of a database and attempts to load it
    from the specified directory. If the database exists, its contents are read from the
    corresponding JSON file and returned along with the database name.

    Parameters:
    directory (dict): A dictionary containing the mapping of database names to their file paths.

    Returns:
    tuple: A tuple containing two elements:
        - The loaded database (dict): The contents of the database as a dictionary.
        - The database name (str): The name of the accessed database.
    
    If the specified database doesn't exist, the function prints an error message and returns None.

    Note:
    - The function uses input() to get the database name from the user.
    - The database files are expected to be in JSON format.
    """
    database_name = input("Ingrese nombre de base de datos.\n\t--> ")
    assert database_name in directory, f"La base de datos {database_name} no existe."
    with open(directory[database_name], 'r') as f:
        database = json.load(f)

    database = str_to_uuid(database)
    return database, database_name


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
    result = reduce(lambda acc, v: acc | {hashable_value(v)}, database1.values(), set())
    result |= reduce(lambda acc, v: acc | {hashable_value(v)}, database2.values(), set())
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

