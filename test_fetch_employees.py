from contextlib import closing
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import fetch_employees


class FetchEmployeesTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database = Path(self.temp_dir.name) / "Employee.db"

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_employee_table(self):
        with closing(sqlite3.connect(self.database)) as connection, connection:
            connection.execute("""
                CREATE TABLE employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    designation TEXT NOT NULL,
                    salary REAL NOT NULL
                )
            """)

    def test_fetches_employee_records(self):
        self.create_employee_table()
        with closing(sqlite3.connect(self.database)) as connection, connection:
            connection.execute(
                "INSERT INTO employees (name, designation, salary) VALUES (?, ?, ?)",
                ("Jane Doe", "Engineer", 72000),
            )

        with patch.object(fetch_employees, "DATABASE", self.database):
            result = fetch_employees.fetch_employees()

        self.assertEqual(result, [(1, "Jane Doe", "Engineer", 72000.0)])

    def test_returns_empty_list_when_table_has_no_records(self):
        self.create_employee_table()

        with patch.object(fetch_employees, "DATABASE", self.database):
            result = fetch_employees.fetch_employees()

        self.assertEqual(result, [])

    def test_raises_error_when_database_is_missing(self):
        with patch.object(fetch_employees, "DATABASE", self.database):
            with self.assertRaises(FileNotFoundError):
                fetch_employees.fetch_employees()

        self.assertFalse(self.database.exists())

    def test_raises_error_when_employees_table_is_missing(self):
        with closing(sqlite3.connect(self.database)):
            pass

        with patch.object(fetch_employees, "DATABASE", self.database):
            with self.assertRaises(sqlite3.OperationalError):
                fetch_employees.fetch_employees()


if __name__ == "__main__":
    unittest.main()