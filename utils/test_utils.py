import pytest
from utils import parse_value

def test_parse_string():
    resultado = parse_value("str.hola mundo")
    assert resultado["_type"] == "str"
    assert resultado["value"] == "hola mundo"

def test_parse_int():
    resultado = parse_value("int.42")
    assert resultado["_type"] == "int"
    assert resultado["value"] == 42

def test_parse_float():
    resultado = parse_value("float.3.14")
    assert resultado["_type"] == "float"
    assert resultado["value"] == 3.14

def test_parse_tuple():
    resultado = parse_value("tuple.a,b,c")
    assert resultado["_type"] == "tuple"
    assert resultado["value"] == ("a", "b", "c")

def test_parse_list():
    resultado = parse_value("list.1,2,3")
    assert resultado["_type"] == "list"
    assert resultado["value"] == ["1", "2", "3"]

def test_parse_set():
    resultado = parse_value("set.A,b,C,a")
    assert resultado["_type"] == "set"
    assert resultado["value"] == {"a", "b", "c"}

def test_parse_matrix():
    resultado = parse_value("matrix.1,2,3;4,5,6;7,8,9")
    assert resultado["_type"] == "matrix"
    assert resultado["value"] == [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]