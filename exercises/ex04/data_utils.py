"""Utility functions for wrangling data."""

__author__ = "730394883"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    csv_reader = DictReader(csv_file)
    for row in csv_reader:
        rows.append(row)
    return rows


def column_values(rows: list[dict[str, str]], key: str) -> list[str]:
    """Read a CSV file's contents into a list of columns."""
    values: list[str] = []
    for row in rows:
        values.append(row[key])
    return values
        
 
def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Read a CSV file's contents into a list of columns."""
    dict_of_columns: dict[str, list[str]] = {}
    for col in rows[0]:
        dict_of_columns[col] = column_values(rows, col)
    return dict_of_columns

        


        








# TODO: Define the other functions here.