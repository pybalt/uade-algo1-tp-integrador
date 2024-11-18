import unittest
from unittest.mock import patch
import uuid
from documents import *

class BaseTestDatabase(unittest.TestCase):

    def setUp(self):
        "Funcion que se ejecuta antes de cada test"
        self.mock_directory = {
            "mascotas": "test/mascotas.json"
        }
        self.content = {
            "UUID(929fb381-c97a-46bf-bf9f-af96d626063e)": {
                "nombre": {"_type": "str", "value": "Negra"},
                "especie": {"_type": "str", "value": "Gato"},
                "edad": {"_type": "int", "value": 3},
                "raza": {"_type": "str", "value": "Siames"}
            },
            "UUID(33c70af2-a121-4cff-ad41-f962c1986157)": {
                "nombre": {"_type": "str", "value": "Duque"},
                "especie": {"_type": "str", "value": "Perro"},
                "edad": {"_type": "int", "value": 5},
                "raza": {"_type": "str", "value": "Labrador"}
            }
        }
        if not os.path.exists("test"):
            os.mkdir("test")
        with open(self.mock_directory["mascotas"], 'w+') as f:
            json.dump(self.content, f)

    def tearDown(self):
        "Funcion que se ejecuta despues de cada test"
        for file in self.mock_directory.values():
            if os.path.exists(file):
                os.remove(file)
        
        # Eliminar el archivo que lista los directorios
        if os.path.exists("test/directory.json"):
            os.remove("test/directory.json")

        # Eliminar el directorio de prueba        
        os.path.exists("test") and os.rmdir("test")

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