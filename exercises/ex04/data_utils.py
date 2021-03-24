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

def column_values(csv_file: str) -> list[dict[str,str]]:
    """Read a CSV file's contents into a list of columns."""
    columns: list[dict[str, str]] = []
    csv_reader = DictReader(csv_file)
    for column in csv_reader:
        columns.append(column)
    return columns

def columnar(data_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Read a CSV file's contents into a list of columns."""
    dict_of_columns: dict[str, list[str]] = {}
    for name in data_rows[0]:
        dict_of_columns.update.key(name)
    for value in data_rows[1: len(data_rows)]:
        dict_of_columns.update.value(value)
    return dict_of_columns


        








# TODO: Define the other functions here.