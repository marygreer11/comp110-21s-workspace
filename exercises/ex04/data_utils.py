"""Utility functions for wrangling data."""

__author__ = "730394883"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open("nc_durham_2015_march_21_to_27.csv", "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        return rows


# TODO: Define the other functions here.