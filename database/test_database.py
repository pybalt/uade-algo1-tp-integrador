import unittest
import os
import json
from database.functions import save, delete

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


class TestSaveFunction(BaseTestDatabase):

    def test_save_mascotas_database(self):
        "Save: Debe guardar el contenido en un archivo JSON"
        with open(self.mock_directory["mascotas"], 'r') as f:
            saved_content = json.load(f)
            self.assertEqual(saved_content, self.content)

    def test_save_empty_database(self):
        "Save: Debe manejar el guardado de una base de datos vacía"
        empty_content = {}
        save(empty_content, "mascotas", self.mock_directory)
        with open(self.mock_directory["mascotas"], 'r') as f:
            saved_content = json.load(f)
            self.assertEqual(saved_content, empty_content)

    def test_save_overwrite_database(self):
        "Save: Debe sobrescribir el contenido existente en el archivo JSON"
        new_content = {
            "UUID(b6e903e6-0b91-4d15-875e-5fd97b1c8e4b)": {
                "nombre": {"_type": "str", "value": "Luna"},
                "especie": {"_type": "str", "value": "Conejo"},
                "edad": {"_type": "int", "value": 2},
                "raza": {"_type": "str", "value": "Holland Lop"}
            }
        }
        save(new_content, "mascotas", self.mock_directory)
        with open(self.mock_directory["mascotas"], 'r') as f:
            saved_content = json.load(f)
            self.assertEqual(saved_content, new_content)

class TestDeleteFunction(BaseTestDatabase):

    def test_delete_mascotas_database(self):
        "Delete: Debe eliminar una base de datos existente"
        file_path = self.mock_directory["mascotas"]
        delete("mascotas", self.mock_directory)
        self.assertNotIn("mascotas", self.mock_directory)
        self.assertFalse(os.path.exists(file_path))

    def test_delete_non_existing_database(self):
        "Delete: Debe lanzar un error si la base de datos no existe"
        with self.assertRaises(AssertionError):
            delete("no_existe", self.mock_directory)

    def test_delete_and_save_directory(self):
        "Delete: Debe eliminar la base de datos y permitir guardar el directorio actualizado"
        file_path = self.mock_directory["mascotas"]
        delete("mascotas", self.mock_directory)
        self.assertNotIn("mascotas", self.mock_directory)
        self.assertFalse(os.path.exists(file_path))
        # Guardar el directorio actualizado
        with open("test/directory.json", 'w') as f:
            json.dump(self.mock_directory, f)
        with open("test/directory.json", 'r') as f:
            saved_directory = json.load(f)
            self.assertEqual(saved_directory, self.mock_directory)

if __name__ == '__main__':
    unittest.main()