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



# TODO: Define the other functions here.