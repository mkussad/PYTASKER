# test_project.py
import unittest
from unittest.mock import patch, MagicMock
from project import add_task, edit_task, mark_completed, mark_incomplete, view_tasks, delete_task, export_to_csv, exit_program

class TestProjectFunctions(unittest.TestCase):
    @patch('builtins.input', side_effect=["Test Task"])
    def test_add_task(self, mock_input):
        with patch('project.conn', MagicMock()), patch('project.cursor', MagicMock()):
            self.assertIsNone(add_task())

    @patch('builtins.input', side_effect=["1", "New Task Name"])  # Provide additional input values
    def test_edit_task(self, mock_input):
        with patch('project.conn', MagicMock()), patch('project.cursor', MagicMock()):
            self.assertIsNone(edit_task())

    @patch('builtins.input', side_effect=["1"])
    def test_mark_completed(self, mock_input):
        with patch('project.conn', MagicMock()), patch('project.cursor', MagicMock()):
            self.assertIsNone(mark_completed())

    @patch('builtins.input', side_effect=["1"])
    def test_mark_incomplete(self, mock_input):
        with patch('project.conn', MagicMock()), patch('project.cursor', MagicMock()):
            self.assertIsNone(mark_incomplete())

    @patch('builtins.input', side_effect=["1"])
    def test_delete_task(self, mock_input):
        with patch('project.conn', MagicMock()), patch('project.cursor', MagicMock()):
            self.assertIsNone(delete_task())

    @patch('builtins.input', side_effect=["test_export.csv"])
    def test_export_to_csv(self, mock_input):
        with patch('project.conn', MagicMock()), patch('project.cursor', MagicMock()):
            self.assertIsNone(export_to_csv())

    def test_exit_program(self):
        with patch('project.conn', MagicMock()), patch('project.cursor', MagicMock()):
            with self.assertRaises(SystemExit) as cm:
                exit_program()
            self.assertEqual(cm.exception.code, None)

if __name__ == '__main__':
    unittest.main()
