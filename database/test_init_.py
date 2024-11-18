import unittest
from unittest.mock import patch, MagicMock
from database import handler  
import console.databases


class TestHandler(unittest.TestCase):

    @patch('console.databases.show_menu')
    @patch('console.databases.list_databases')
    def test_option_a_list_databases(self, mock_list_databases, mock_show_menu):
        mock_show_menu.return_value = "a"
        directory = "mock_directory"

        result = handler(directory)

        mock_list_databases.assert_called_once_with(directory)
        self.assertEqual(result, "a")

    @patch('documents.handler')
    @patch('your_module.access')
    @patch('console.databases.show_menu')
    def test_option_b_access_documents(self, mock_show_menu, mock_access, mock_documents_handler):
        mock_show_menu.return_value = "b"
        mock_access.return_value = ("mock_database", "mock_db_name")
        directory = "mock_directory"

        result = handler(directory)

        mock_access.assert_called_once_with(directory)
        mock_documents_handler.assert_called_once_with("mock_database", "mock_db_name")
        self.assertEqual(result, "b")

    @patch('builtins.input', return_value='test_db')
    @patch('your_module.create')
    @patch('console.databases.show_menu')
    def test_option_c_create_database(self, mock_show_menu, mock_create, mock_input):
        mock_show_menu.return_value = "c"
        directory = "mock_directory"

        result = handler(directory)

        mock_create.assert_called_once_with('test_db', directory)
        self.assertEqual(result, "c")

    @patch('console.exit')
    @patch('console.databases.show_menu')
    def test_option_exit(self, mock_show_menu, mock_exit):
        mock_show_menu.return_value = "exit()"
        directory = "mock_directory"

        result = handler(directory)

        mock_exit.assert_called_once()
        self.assertEqual(result, "exit()")

    @patch('console.databases.show_menu')
    def test_unhandled_exception(self, mock_show_menu):
        mock_show_menu.side_effect = Exception("Unexpected error")
        directory = "mock_directory"

        with patch('console.error') as mock_error, patch('console.pause_program'):
            result = handler(directory)
            mock_error.assert_called_once_with("Unexpected error")
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
