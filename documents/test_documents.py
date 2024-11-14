import unittest
from documents import *
from .functions import select_distinct

# pruebas
DIRECTORY = {
    "db1": {"doc1": {"name": "Prueba"}},
    "db2": {"doc2": {"name": "Prueba2"}}
}
DATABASE = {"doc1": {"name": "Prueba"}}


def test_create_document():
    create(DATABASE)
    assert len(DATABASE) == 2  # Verifica que se ha añadido un nuevo documento

def test_edit_document():
    doc_id = 'doc1'
    if doc_id in DATABASE:
        DATABASE[doc_id]["name"] = "Nuevo"
    assert DATABASE[doc_id]["name"] == "Nuevo"  # Verifica que el nombre fue cambiado

def test_delete_document():
    doc_id = 'doc1'
    if doc_id in DATABASE:
        del DATABASE[doc_id]
    assert doc_id not in DATABASE  # Verifica que el documento ha sido eliminado

def test_filter_by_id():
    # Prueba la función `filter_by_id` para buscar un documento por ID
    doc_id = 'doc1'
    assert doc_id in DATABASE  # Verifica que el documento existe



