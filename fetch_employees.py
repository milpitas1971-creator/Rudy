from contextlib import closing
import sqlite3
from pathlib import Path

DATABASE = Path(__file__).with_name("Employee.db")


def fetch_employees():
    if not DATABASE.exists():
        raise FileNotFoundError(f"Database not found: {DATABASE}")

    with closing(sqlite3.connect(DATABASE)) as connection:
        return connection.execute(
            "SELECT id, name, designation, salary FROM employees"
        ).fetchall()


if __name__ == "__main__":
    try:
        employees = fetch_employees()
        if employees:
            for employee in employees:
                print(employee)
        else:
            print("No employee records found.")
    except (FileNotFoundError, sqlite3.Error) as error:
        print(f"Could not fetch employees: {error}")