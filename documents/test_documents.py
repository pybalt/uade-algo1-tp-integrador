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