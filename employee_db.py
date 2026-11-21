import sqlite3
from pathlib import Path

DATABASE = Path(__file__).with_name("Employee.db")


def create_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                designation TEXT NOT NULL,
                salary REAL NOT NULL
            )
        """)


def add_employee(name, designation, salary):
    with sqlite3.connect(DATABASE) as connection:
        connection.execute(
            "INSERT INTO employees (name, designation, salary) VALUES (?, ?, ?)",
            (name, designation, salary),
        )


if __name__ == "__main__":
    create_database()
    name = input("Employee name: ").strip()
    designation = input("Designation: ").strip()
    salary = float(input("Salary: "))

    add_employee(name, designation, salary)
    print("Employee added.")