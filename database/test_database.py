import os
import json
import pytest
from database.functions import save, delete

@pytest.fixture
def setup_mock_directory():
    "Fixture que se ejecuta antes de cada test"
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
    
    # Se retorna el directorio y el contenido de la base de datos
    # Para ser accedidos en los tests
    yield mock_directory, content
    # Luego de ejecutar el test, se eliminan los archivos creados,
    # para que no interfieran con otros tests
    # y para limpiar el ambiente
    for file in mock_directory.values():
        if os.path.exists(file):
            os.remove(file)
    if os.path.exists("test/directory.json"):
        os.remove("test/directory.json")
    if os.path.exists("test"):
        os.rmdir("test")

def test_save_mascotas_database(setup_mock_directory):
    "Save: Debe guardar el contenido en un archivo JSON"
    mock_directory, content = setup_mock_directory
    with open(mock_directory["mascotas"], 'r') as f:
        saved_content = json.load(f)
        assert saved_content == content

def test_save_empty_database(setup_mock_directory):
    "Save: Debe manejar el guardado de una base de datos vacía"
    mock_directory, _ = setup_mock_directory
    empty_content = {}
    save(empty_content, "mascotas", mock_directory)
    with open(mock_directory["mascotas"], 'r') as f:
        saved_content = json.load(f)
        assert saved_content == empty_content

def test_save_overwrite_database(setup_mock_directory):
    "Save: Debe sobrescribir el contenido existente en el archivo JSON"
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
    "Delete: Debe eliminar una base de datos existente"
    mock_directory, _ = setup_mock_directory
    file_path = mock_directory["mascotas"]
    delete("mascotas", mock_directory)
    assert "mascotas" not in mock_directory
    assert not os.path.exists(file_path)

def test_delete_non_existing_database(setup_mock_directory):
    "Delete: Debe lanzar un error si la base de datos no existe"
    mock_directory, _ = setup_mock_directory
    with pytest.raises(AssertionError):
        delete("no_existe", mock_directory)

def test_delete_and_save_directory(setup_mock_directory):
    "Delete: Debe eliminar la base de datos y permitir guardar el directorio actualizado"
    mock_directory, _ = setup_mock_directory
    file_path = mock_directory["mascotas"]
    delete("mascotas", mock_directory)
    assert "mascotas" not in mock_directory
    assert not os.path.exists(file_path)
    # Guardar el directorio actualizado
    with open("test/directory.json", 'w') as f:
        json.dump(mock_directory, f)
    with open("test/directory.json", 'r') as f:
        saved_directory = json.load(f)
        assert saved_directory == mock_directory
