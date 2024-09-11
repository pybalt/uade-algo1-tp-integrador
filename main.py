import sys


def get_databases() -> list:
    """
    Retrieves a list of databases.

    Returns:
        list: A list of databases.
    """
    databases = {"pepe": {}}
    return databases


def create_database(name: str, directory):
    databases[name] = {}


def list_databases(directory) -> None:
    for db in directory:
        print(db)


def access_database(directory): ...


def get_choices() -> dict:
    choices = {"a": list_databases, "b": access_database}
    return choices


def list_choices(choices: dict) -> None:
    print("Sus opciones son")
    explanations = {
        "A": "Listar bases de datos",
        "B": "Acceder directamente a una base de datos",
        "exit()": "Salir del programa",
    }
    for key in explanations:
        print(f"\t{key}: {explanations[key]}")


def handle_options(choices) -> None:

    list_choices(choices)
    user_input = input("Seleccione una opcion\n\t--> ")
    if user_input == "exit()":
        exit()
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
