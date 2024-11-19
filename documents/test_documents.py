import pytest
import uuid
from documents import create, select_distinct, search_by_regex, edit, delete, filter_by_id

@pytest.fixture
def database():
    return {"doc1": {"name": {'_type': 'str', 'value': 'Prueba'}}}
    
def test_create_document(monkeypatch, database):
    """Create: Should create a new document in the database with the fields provided by the user."""
    inputs = iter(["name", "str.NuevoDoc", "exit()"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    new_doc_id = create(database)
    
    assert len(database) == 2
    assert new_doc_id in database
    assert database[new_doc_id]["name"] == {'_type': 'str', 'value': 'NuevoDoc'}
    
def test_select_distinct_count():
    """Select distinct: Should identify and count unique documents in the database."""
    database = {
        "doc1": {"prueba": "Y"},
        "doc2": {"prueba": "X"},
        "doc3": {"prueba": "Y"},  
    }
    distinct_docs = select_distinct(database)
    
    assert len(distinct_docs) == 2
    
def test_select_distinct_content():
    """Select distinct: Should verify that unique documents contain the expected values."""
    database = {
        "doc1": {"prueba": "Y"},
        "doc2": {"prueba": "X"},
        "doc3": {"prueba": "Y"},  
    }
    distinct_docs = select_distinct(database)
    
    assert any(doc["prueba"] == "Y" for doc in distinct_docs.values())
    assert any(doc["prueba"] == "X" for doc in distinct_docs.values())
    
def test_search_by_regex(monkeypatch):
    """Search by regex: Should find documents whose values match a valid regular expression."""
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
    """Search by regex: Should raise an error if an invalid regular expression is entered."""
    monkeypatch.setattr('builtins.input', lambda _: "*invalid[regex")
    
    with pytest.raises(ValueError, match="Expresión regular inválida"):
        search_by_regex(database)

def test_search_recursive_with_list(monkeypatch):
    """Search by regex: Should search for matching values in lists and nested structures."""
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

def test_edit_document(monkeypatch, database):
    """Edit: Should edit a specific field of an existing document."""
    doc_id = uuid.uuid4()
    database[doc_id] = {"name": "Original"}

    inputs = iter([str(doc_id), "name", "str.Editado"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = edit(database)
    
    assert result is True
    assert database[doc_id]["name"] == {'_type': 'str', 'value': 'Editado'}

def test_delete_nonexistent_document(monkeypatch, database):
    """Edit: Should return False if attempting to edit a non-existent document."""
    monkeypatch.setattr('builtins.input', lambda _: str(uuid.uuid4()))
    
    with pytest.raises(KeyError, match="No se encontró ningún documento con el ID"):
        delete(database)

def test_delete_document(monkeypatch, database):
    """Delete: Should delete an existing document from the database."""
    doc_id = uuid.uuid4()
    database[doc_id] = {"name": "ParaEliminar"}

    monkeypatch.setattr('builtins.input', lambda _: str(doc_id))
    delete(database)
    
    assert doc_id not in database

def test_delete_nonexistent_document(monkeypatch, database):
    """Delete: Should raise an error if attempting to delete a non-existent document."""
    monkeypatch.setattr('builtins.input', lambda _: str(uuid.uuid4()))
    
    with pytest.raises(KeyError, match=r"No se encontró ningún documento con el ID: .*"):
        delete(database)

def test_filter_by_id(monkeypatch, database):
    """Filter by ID: Should return the document with the specified ID if it exists."""
    doc_id = uuid.uuid4()
    database[doc_id] = {"name": "Prueba"}

    monkeypatch.setattr('builtins.input', lambda _: str(doc_id))
    result_id, document = filter_by_id(database)
    
    assert result_id == doc_id
    assert document["name"] == "Prueba"

def test_filter_by_nonexistent_id(monkeypatch, database):
    """Filter by ID: Should raise an error if the specified ID does not exist in the database."""
    monkeypatch.setattr('builtins.input', lambda _: str(uuid.uuid4()))
    
    with pytest.raises(KeyError, match="No se encontró ningún documento con el ID"):
        filter_by_id(database)