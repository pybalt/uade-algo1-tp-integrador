documentos = [
    {"id": "doc1", "contenido": "Documento 1"},
    {"id": "doc2", "contenido": "Documento 2"},
    {"id": "doc3", "contenido": "Documento 3"},
]

# Función para filtrar por ID
def filtrar_por_id(documentos):
    # Solicitar al usuario que ingrese el ID
    id_usuario = input("Introducir el id del documento: ")

    # Filtrar el documento que coincide con el ID introducido
    resultado = [doc for doc in documentos if doc["id"] == id_usuario]

    # Verificar si se encontró un documento o no
    if resultado:
        # Mostrar el documento encontrado, con el ID como tupla
        print({"id": (resultado[0]["id"],), "contenido": resultado[0]["contenido"]})
    else:
        print(f"No se encontró ningún documento con el ID: {id_usuario}")

#Llamar a la función
filtrar_por_id(documentos)