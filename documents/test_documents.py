from unittest.mock import patch
import uuid
from documents import *


DATABASE = {"doc1": {"name": "Prueba"}}

def test_create_document():
    with patch('builtins.input', side_effect=[
        "name",  
        "str.NuevoDoc",  
        "exit()"  
    ]):
        new_doc_id = create(DATABASE)
    
    
    assert len(DATABASE) == 2  
    assert new_doc_id in DATABASE  
    
    
    assert DATABASE[new_doc_id]["name"] == {'_type': 'str', 'value': 'NuevoDoc'}

def test_select_distinct():
    database = {
        "doc1": {"prueba": "Y"},
        "doc2": {"prueba": "X"},
        "doc3": {"prueba": "Y"},  
    }
    distinct_docs = select_distinct(database)
    
    assert len(distinct_docs) == 2  
    
    assert any(doc["prueba"] == "Y" for doc in distinct_docs.values())
    assert any(doc["prueba"] == "X"for doc in distinct_docs.values())

def test_search_by_regex():
    database = {
        "doc1": {"prueba": "X"},
        "doc2": {"prueba": "XY"},
        "doc3": {"prueba": "Y"},
    }

    with patch('builtins.input', return_value="X"):
        with patch('builtins.print') as mock_print:
            matches = search_by_regex(database)
            
            assert matches == True

            mock_print.assert_any_call("Document found with ID: doc1")
            mock_print.assert_any_call("Document found with ID: doc2")

def test_edit_document():
    doc_id = 'doc1'
    if doc_id in DATABASE:
        DATABASE[doc_id]["name"] = "Nuevo"
    assert DATABASE[doc_id]["name"] == "Nuevo"  

def test_delete_document():
    doc_id = 'doc1'
    if doc_id in DATABASE:
        del DATABASE[doc_id]
    assert doc_id not in DATABASE 

def test_filter_by_id():
    doc_id = uuid.uuid4()  
    DATABASE[doc_id] = {"name": "Prueba"}

    with patch('builtins.input', return_value=str(doc_id)):  
        result_id, document = filter_by_id(DATABASE)
    
    assert result_id == doc_id  
    assert document["name"] == "Prueba" 