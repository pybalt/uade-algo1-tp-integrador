from .functions import *
import console.documents


def handler(database: dict) -> None:
    """
    Provides options to operate within the selected database.

    Parameters:
    - database (dict): The current database being operated on.

    Returns:
    None
    """
    # TODO: Reformat this function to use the console module. documents.__init__.handler
    # TODO: Reformat try-except blocks to use console.error and console.log. documents.__init__.handler

    console.documents.show_menu()
    option = input("Seleccione una opción:\n\t--> ")
    try:
        while option != "exit()":
            if option == "1":
                console.log("Creando un nuevo documento...\n"
                            +"Los tipos de datos soportados son: string, int, float, tuple, list, set, matrix\n"
                            +"El formato de entrada es 'tipo.valor1,valor2,...'\n"
                            +"Para los tipos de datos tales como set, tuple, list y matrix, separe los valores con comas.\n"
                            +"Ademas, para los tipos de datos como matrix, separe las filas con punto y coma.\n"
                )
                document_id = create(database)
                console.log(f"Documento creado con ID: {document_id}")
            elif option == "2":
                console.documents.list_documents(database)
            elif option == "3":
                delete(database)
            elif option == "4":
                try:
                    id, doc = filter_by_id(database)
                    console.log(f"Documento encontrado: {doc}")
                except KeyError:
                    console.error(f"No se encontró ningún documento con el ID: {id}")
            elif option == "5":
                if edit(database):
                    console.log(f"Documento actualizado: {doc}")
                else: 
                    console.error(f"No se encontró ningún documento con el ID: {id}")
            elif option == "6":
                docs = search_by_regex(database)
                if docs:
                    console.log("Se encontraron documentos que coinciden con el patrón.")
                    console.documents.list_documents(docs)
                else:
                    console.error("No se encontraron documentos que coinciden con el patrón.")
            elif option == "7":
                unique_documents = select_distinct(database)
                console.log("Documentos únicos en la base de datos:")
                console.documents.list_documents(unique_documents)

            console.documents.show_menu()
            option = input("Seleccione una opción:\n\t--> ")
    except AssertionError as e:
        console.error(e)