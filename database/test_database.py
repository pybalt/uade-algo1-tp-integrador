import os
import json
import pytest
import uuid
from database.functions import (
    save, create, delete,access,
    union,hashable_value,frozenset_to_readable,
    intersection, difference, symmetric_difference,
    str_to_uuid, uuid_to_str
    )

@pytest.fixture
def setup_mock_directory():
    """Fixture that runs before each test"""
    mock_directory = {
        "mascotas": "test/mascotas.json"
    }
    content = {
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
    with open(mock_directory["mascotas"], 'w+') as f:
        json.dump(content, f)
    
    # Return the directory and database content
    # To be accessed in the tests
    yield mock_directory, content
    # After executing the test, delete the created files,
    # so they do not interfere with other tests
    # and to clean the environment
    for file in mock_directory.values():
        if os.path.exists(file):
            os.remove(file)
    if os.path.exists("test/directory.json"):
        os.remove("test/directory.json")
    if os.path.exists("test"):
        os.rmdir("test")

def test_create_new_database(setup_mock_directory):
    "Create: Should create a new database with the specified name"
    mock_directory, _ = setup_mock_directory
    create("nueva_base", mock_directory)
    
    assert "nueva_base" in mock_directory
    assert os.path.exists(mock_directory["nueva_base"])
    
    with open(mock_directory["nueva_base"], 'r') as f:
        content = json.load(f)
        assert content == {}

def test_create_existing_database(setup_mock_directory):
    "Create: Should raise an error if the database already exists"
    mock_directory, _ = setup_mock_directory
    with pytest.raises(AssertionError):
        create("mascotas", mock_directory)

def test_save_mascotas_database(setup_mock_directory):
    "Save: Should save the content to a JSON file"
    mock_directory, content = setup_mock_directory
    with open(mock_directory["mascotas"], 'r') as f:
        saved_content = json.load(f)
        assert saved_content == content

def test_save_empty_database(setup_mock_directory):
    "Save: Should handle saving an empty database"
    mock_directory, _ = setup_mock_directory
    empty_content = {}
    save(empty_content, "mascotas", mock_directory)
    with open(mock_directory["mascotas"], 'r') as f:
        saved_content = json.load(f)
        assert saved_content == empty_content

def test_save_overwrite_database(setup_mock_directory):
    "Save: Should overwrite the existing content in the JSON file"
    mock_directory, _ = setup_mock_directory
    new_content = {
        "UUID(b6e903e6-0b91-4d15-875e-5fd97b1c8e4b)": {
            "nombre": {"_type": "str", "value": "Luna"},
            "especie": {"_type": "str", "value": "Conejo"},
            "edad": {"_type": "int", "value": 2},
            "raza": {"_type": "str", "value": "Holland Lop"}
        }
    }
    save(new_content, "mascotas", mock_directory)
    with open(mock_directory["mascotas"], 'r') as f:
        saved_content = json.load(f)
        assert saved_content == new_content

def test_delete_mascotas_database(setup_mock_directory):
    "Delete: Should delete an existing database"
    mock_directory, _ = setup_mock_directory
    file_path = mock_directory["mascotas"]
    delete("mascotas", mock_directory)
    assert "mascotas" not in mock_directory
    assert not os.path.exists(file_path)

def test_delete_non_existing_database(setup_mock_directory):
    "Delete: Should raise an error if the database does not exist"
    mock_directory, _ = setup_mock_directory
    with pytest.raises(AssertionError):
        delete("no_existe", mock_directory)

def test_delete_and_save_directory(setup_mock_directory):
    "Delete: Should delete the database and allow saving the updated directory"
    mock_directory, _ = setup_mock_directory
    file_path = mock_directory["mascotas"]
    delete("mascotas", mock_directory)
    assert "mascotas" not in mock_directory
    assert not os.path.exists(file_path)
    # Save the updated directory
    with open("test/directory.json", 'w') as f:
        json.dump(mock_directory, f)
    with open("test/directory.json", 'r') as f:
        saved_directory = json.load(f)
        assert saved_directory == mock_directory

def test_hashable_value_dict():
    "hashable_value: Should convert a dictionary to a hashable object"
    value = {
        "nombre": "Max",
        "edad": 4,
        "raza": "Bulldog"
    }
    result = hashable_value(value)
    assert isinstance(result, frozenset)

def test_hashable_value_list():
    "hashable_value: Should convert a list to a hashable object"
    value = ["Max", "Bulldog", 4]
    result = hashable_value(value)
    assert isinstance(result, tuple)

def test_hashable_value_primitive():
    "hashable_value: Should return the original value if it is a primitive type"
    result = hashable_value("Max")
    assert result == "Max"

def test_frozenset_to_readable_dict():
    "frozenset_to_readable: Should convert a frozenset back to a readable dictionary"
    value = frozenset({
        ("nombre", "Max"),
        ("edad", 4),
        ("raza", "Bulldog")
    })
    result = frozenset_to_readable(value)
    assert isinstance(result, dict)
    assert result == {"nombre": "Max", "edad": 4, "raza": "Bulldog"}

def test_frozenset_to_readable_list():
    "frozenset_to_readable: Should convert a frozenset of tuples to a readable list"
    value = frozenset([("nombre", "Max"), ("edad", 4), ("raza", "Bulldog")])
    result = frozenset_to_readable(value)
    assert result == {"nombre": "Max", "edad": 4, "raza": "Bulldog"}

def test_str_to_uuid():
    "str_to_uuid: Should convert string UUID keys to uuid.UUID"
    data = {
        "UUID(929fb381-c97a-46bf-bf9f-af96d626063e)": "valor1",
        "otra_clave": "valor2"
    }
    result = str_to_uuid(data)
    
    expected_key = uuid.UUID("929fb381-c97a-46bf-bf9f-af96d626063e")
    
    assert isinstance(list(result.keys())[0], uuid.UUID)
    
    assert result[expected_key] == "valor1"
    
    assert result["otra_clave"] == "valor2"

def test_uuid_to_str():
    "uuid_to_str: Should convert uuid.UUID keys back to strings in the format 'UUID(...)'"
    data = {
        uuid.UUID("929fb381-c97a-46bf-bf9f-af96d626063e"): "valor1",
        "otra_clave": "valor2"
    }
    result = uuid_to_str(data)
    assert isinstance(list(result.keys())[0], str)
    assert list(result.keys())[0] == "UUID(929fb381-c97a-46bf-bf9f-af96d626063e)"
    assert result["UUID(929fb381-c97a-46bf-bf9f-af96d626063e)"] == "valor1"
    assert result["otra_clave"] == "valor2"

def test_union_databases(setup_mock_directory):
    """Union: Should perform the union of two databases."""
    mock_directory, content = setup_mock_directory
    second_content = {
        "UUID(8b9b3915-4793-4628-8c52-4be1c456d575)": {
            "nombre": {"_type": "str", "value": "Max"},
            "especie": {"_type": "str", "value": "Perro"},
            "edad": {"_type": "int", "value": 4},
            "raza": {"_type": "str", "value": "Bulldog"}
        }
    }

    union_result = union(content, second_content)
    expected_documents = list(content.values()) + list(second_content.values())

    assert len(union_result) == len(expected_documents), "The union result does not contain the expected number of documents."
    for doc in expected_documents:
        assert doc in union_result, f"The document {doc} is missing in the union result."
def test_intersection_databases(setup_mock_directory):
    "Intersection: Should return the intersection of two databases"
    mock_directory, content = setup_mock_directory
    second_content = {
        "UUID(929fb381-c97a-46bf-bf9f-af96d626063e)": {
            "nombre": {"_type": "str", "value": "Negra"},
            "especie": {"_type": "str", "value": "Gato"},
            "edad": {"_type": "int", "value": 3},
            "raza": {"_type": "str", "value": "Siames"}
        },
        "UUID(8b9b3915-4793-4628-8c52-4be1c456d575)": {
            "nombre": {"_type": "str", "value": "Max"},
            "especie": {"_type": "str", "value": "Perro"},
            "edad": {"_type": "int", "value": 4},
            "raza": {"_type": "str", "value": "Bulldog"}
        }
    }
    result = intersection(content, second_content)
    assert len(result) == 1  

def test_difference_databases(setup_mock_directory):
    "Difference: Should return the difference between two databases"
    mock_directory, content = setup_mock_directory
    second_content = {
        "UUID(8b9b3915-4793-4628-8c52-4be1c456d575)": {
            "nombre": {"_type": "str", "value": "Max"},
            "especie": {"_type": "str", "value": "Perro"},
            "edad": {"_type": "int", "value": 4},
            "raza": {"_type": "str", "value": "Bulldog"}
        }
    }
    result = difference(content, second_content)
    assert len(result) == 2

def test_symmetric_difference_databases(setup_mock_directory):
    "Symmetric Difference: Should return the symmetric difference between two databases"
    mock_directory, content = setup_mock_directory
    second_content = {
        "UUID(8b9b3915-4793-4628-8c52-4be1c456d575)": {
            "nombre": {"_type": "str", "value": "Max"},
            "especie": {"_type": "str", "value": "Perro"},
            "edad": {"_type": "int", "value": 4},
            "raza": {"_type": "str", "value": "Bulldog"}
        }
    }
    result = symmetric_difference(content, second_content)
    assert len(result) == 3  
