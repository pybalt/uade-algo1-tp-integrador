import pytest
from database import documents
from unittest.mock import patch, MagicMock
from database import handler
import console.databases


@patch(console.databases.show_menu)
@patch(console.databases.list_databases)
def test_option_a_list_databases(mock_list_databases, mock_show_menu):
    # Simula que el usuario selecciona la opción "a"
    mock_show_menu.return_value = "a"
    directory = "mock_directory"

    # Ejecuta la función handler
    result = handler(directory)

    # Verifica que la función list_databases fue llamada
    mock_list_databases.assert_called_once_with(directory)
    assert result == "a"


# Test para la opción "b"
@patch(documents.handler)
@patch(console.databases)
@patch(console.databases.show_menu)
def test_option_b_access_documents(mock_show_menu, mock_access, mock_documents_handler):
    # Simula que el usuario selecciona la opción "b"
    mock_show_menu.return_value = "b"
    mock_access.return_value = ("mock_database", "mock_db_name")
    directory = "mock_directory"

    # Ejecuta la función handler
    result = handler(directory)

    # Verifica que las funciones se llamaron correctamente
    mock_access.assert_called_once_with(directory)
    mock_documents_handler.assert_called_once_with("mock_database", "mock_db_name")
    assert result == "b"


# Test para la opción "c"
@patch(console.log, return_value='test_db')
@patch(handler.create)
@patch(console.databases.show_menu)
def test_option_c_create_database(mock_show_menu, mock_create, mock_input):
    # Simula que el usuario selecciona la opción "c"
    mock_show_menu.return_value = "c"
    directory = "mock_directory"

    # Ejecuta la función handler
    result = handler(directory)

    # Verifica que la función create fue llamada
    mock_create.assert_called_once_with('test_db', directory)
    assert result == "c"


# Test para la opción "exit()"
@patch(console.exit)
@patch(console.databases.show_menu)
def test_option_exit(mock_show_menu, mock_exit):
    # Simula que el usuario selecciona "exit()"
    mock_show_menu.return_value = "exit()"
    directory = "mock_directory"

    # Ejecuta la función handler
    result = handler(directory)

    # Verifica que la función exit fue llamada
    mock_exit.assert_called_once()
    assert result == "exit()"


# Test para manejar una excepción no esperada
@patch(console.databases.show_menu)
def test_unhandled_exception(mock_show_menu):
    # Simula un error inesperado
    mock_show_menu.side_effect = Exception("Unexpected error")
    directory = "mock_directory"

    with patch('console.error') as mock_error, patch('console.pause_program'):
        result = handler(directory)
        mock_error.assert_called_once_with("Unexpected error")
        assert result is None

