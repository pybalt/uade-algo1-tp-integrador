documentos = [
    {"id": "doc1", "contenido": "Documento 1"},
    {"id": "doc2", "contenido": "Documento 2"},
    {"id": "doc3", "contenido": "Documento 3"},
]

# Generar listado utilizando comprensión de listas
listado = [(indice, doc["id"]) for indice, doc in enumerate(documentos)]

# Imprimir el listado en el formato requerido
for indice, doc_id in listado:
    print(f"Índice: {indice}, ID del documento: {doc_id}")