import unittest
from utils import parse_value

class TestParseValue(unittest.TestCase):
    def test_parse_string(self):
        resultado = parse_value("string.hola mundo")
        self.assertEqual(resultado["_type"], "string")
        self.assertEqual(resultado["value"], "hola mundo")

    def test_parse_int(self):
        resultado = parse_value("int.42")
        self.assertEqual(resultado["_type"], "int")
        self.assertEqual(resultado["value"], 42)

    def test_parse_float(self):
        resultado = parse_value("float.3.14")
        self.assertEqual(resultado["_type"], "float")
        self.assertEqual(resultado["value"], 3.14)

    def test_parse_tuple(self):
        resultado = parse_value("tuple.a,b,c")
        self.assertEqual(resultado["_type"], "tuple")
        self.assertEqual(resultado["value"], ("a", "b", "c"))

    def test_parse_list(self):
        resultado = parse_value("list.1,2,3")
        self.assertEqual(resultado["_type"], "list")
        self.assertEqual(resultado["value"], ["1", "2", "3"])

    def test_parse_set(self):
        resultado = parse_value("set.A,b,C,a")
        self.assertEqual(resultado["_type"], "set")
        self.assertEqual(resultado["value"], {"a", "b", "c"})

    def test_parse_matrix(self):
        resultado = parse_value("matrix.1,2,3;4,5,6;7,8,9")
        self.assertEqual(resultado["_type"], "matrix")
        self.assertEqual(resultado["value"], [["1","2","3"], ["4","5","6"], ["7","8","9"]])

if __name__ == '__main__':
    unittest.main()