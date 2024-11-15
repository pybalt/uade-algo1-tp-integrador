import unittest
import os
import json
from database.functions import save, delete


class TestSaveFunction(unittest.TestCase):

    def setUp(self):
        self.mock_directory = {
            "animales": "data/animales.json",
            "mascotas": "data/directory.json"
        }
        os.makedirs(os.path.dirname(self.mock_directory["animales"]), exist_ok=True)
        os.makedirs(os.path.dirname(self.mock_directory["mascotas"]), exist_ok=True)


    def test_save_mascotas_database(self): 
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
            },
            "UUID(b6e903e6-0b91-4d15-875e-5fd97b1c8e4b)": {
                "nombre": {"_type": "str", "value": "Luna"},
                "especie": {"_type": "str", "value": "Conejo"},
                "edad": {"_type": "int", "value": 2},
                "raza": {"_type": "str", "value": "Holland Lop"}
            },
            "UUID(6bcd9425-d201-4543-87d1-b3816871ce52)": {
                "nombre": {"_type": "str", "value": "Max"},
                "especie": {"_type": "str", "value": "Hamster"},
                "edad": {"_type": "int", "value": 1},
                "raza": {"_type": "str", "value": "Sirio"}
            },
            "UUID(2fc72c55-7fa0-4ad7-a168-7275eecfa7d7)": {
                "nombre": {"_type": "str", "value": "Bella"},
                "especie": {"_type": "str", "value": "Pajaro"},
                "edad": {"_type": "int", "value": 4},
                "raza": {"_type": "str", "value": "Canario"}
            }
        }
        save(content, "mascotas", self.mock_directory)
        with open(self.mock_directory["mascotas"], 'r') as f:
            saved_content = json.load(f)
            self.assertEqual(saved_content, content)

    def test_delete_mascotas_database(self):
        delete("mascotas", self.mock_directory)
        self.assertNotIn("mascotas", self.mock_directory)
        self.assertFalse(os.path.exists(self.mock_directory["mascotas"]))
    

if __name__ == '_main_':
    unittest.main()