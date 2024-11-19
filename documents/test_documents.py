import pytest
import uuid
from documents import *

DATABASE = {"doc1": {"name": "Prueba"}}

def test_create_document(monkeypatch):
    """Create: Debe crear un nuevo documento en la base de datos con los campos proporcionados por el usuario."""
    inputs = iter(["name", "str.NuevoDoc", "exit()"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    new_doc_id = create(DATABASE)
    
    assert len(DATABASE) == 2
    assert new_doc_id in DATABASE
    assert DATABASE[new_doc_id]["name"] == {'_type': 'str', 'value': 'NuevoDoc'}

def test_select_distinct_count():
    """Select distinct: Debe identificar y contar documentos únicos en la base de datos."""
    database = {
        "doc1": {"prueba": "Y"},
        "doc2": {"prueba": "X"},
        "doc3": {"prueba": "Y"},  
    }
    distinct_docs = select_distinct(database)
    
    assert len(distinct_docs) == 2

def test_select_distinct_content():
    """Select distinct: Debe verificar que los documentos únicos contienen los valores esperados."""
    database = {
        "doc1": {"prueba": "Y"},
        "doc2": {"prueba": "X"},
        "doc3": {"prueba": "Y"},  
    }
    distinct_docs = select_distinct(database)
    
    assert any(doc["prueba"] == "Y" for doc in distinct_docs.values())
    assert any(doc["prueba"] == "X" for doc in distinct_docs.values())

def test_search_by_regex(monkeypatch):
    """Search by regex: Debe encontrar documentos cuyos valores coincidan con una expresión regular válida."""
    database = {
        "doc1": {"prueba": "X"},
        "doc2": {"prueba": "XY"},
        "doc3": {"prueba": "Y"},
    }

    monkeypatch.setattr('builtins.input', lambda _: "X")
    matches = search_by_regex(database)
    
    assert isinstance(matches, dict)
    assert len(matches) == 2
    assert "doc1" in matches
    assert "doc2" in matches
    assert "doc3" not in matches

def test_search_by_regex_invalid_pattern(monkeypatch):
    """Search by regex: Debe lanzar un error si se ingresa una expresión regular inválida."""
    monkeypatch.setattr('builtins.input', lambda _: "*invalid[regex")
    
    with pytest.raises(ValueError, match="Expresión regular inválida"):
        search_by_regex(DATABASE)

def test_search_recursive_with_list(monkeypatch):
    """Search by regex: Debe buscar valores coincidentes en listas y estructuras anidadas."""
    database = {
        "doc1": {"prueba": ["X", "Y", "Z"]},  
        "doc2": {"prueba": ["A", "B", "C"]},  
        "doc3": {"prueba": "XY"}              
    }

    monkeypatch.setattr('builtins.input', lambda _: "X")
    matches = search_by_regex(database)
    
    assert isinstance(matches, dict)
    assert len(matches) == 2
    assert "doc1" in matches
    assert "doc3" in matches

def test_edit_document(monkeypatch):
    """Edit: Debe editar un campo específico de un documento existente."""
    doc_id = uuid.uuid4()
    DATABASE[doc_id] = {"name": "Original"}

    inputs = iter([str(doc_id), "name", "str.Editado"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = edit(DATABASE)
    
    assert result is True
    assert DATABASE[doc_id]["name"] == {'_type': 'str', 'value': 'Editado'}

def test_edit_nonexistent_document(monkeypatch):
    """Edit: Debe devolver False si se intenta editar un documento inexistente."""
    inputs = iter([str(uuid.uuid4()), "name", "NuevoValor"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = edit(DATABASE)
    
    assert result is False

def test_delete_document(monkeypatch):
    """Delete: Debe eliminar un documento existente de la base de datos."""
    doc_id = uuid.uuid4()
    DATABASE[doc_id] = {"name": "ParaEliminar"}

    monkeypatch.setattr('builtins.input', lambda _: str(doc_id))
    delete(DATABASE)
    
    assert doc_id not in DATABASE

def test_delete_nonexistent_document(monkeypatch):
    """Delete: Debe lanzar un error si se intenta eliminar un documento inexistente."""
    monkeypatch.setattr('builtins.input', lambda _: str(uuid.uuid4()))
    
    with pytest.raises(KeyError, match="No se encontró ningún documento con el ID"):
        delete(DATABASE)

def test_filter_by_id(monkeypatch):
    """Filter by ID: Debe devolver el documento con el ID especificado si existe."""
    doc_id = uuid.uuid4()
    DATABASE[doc_id] = {"name": "Prueba"}

    monkeypatch.setattr('builtins.input', lambda _: str(doc_id))
    result_id, document = filter_by_id(DATABASE)
    
    assert result_id == doc_id
    assert document["name"] == "Prueba"

def test_filter_by_nonexistent_id(monkeypatch):
    """Filter by ID: Debe lanzar un error si el ID especificado no existe en la base de datos."""
    monkeypatch.setattr('builtins.input', lambda _: str(uuid.uuid4()))
    
    with pytest.raises(KeyError, match="No se encontró ningún documento con el ID"):
        filter_by_id(DATABASE)