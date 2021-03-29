"""Utility functions for wrangling data."""

__author__ = "730388741"

from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows.""" 
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    table: list[dict[str, str]] = []
    for row in csv_reader:
        table.append(row)
    file_handle.close()
    return table


def column_values(row_list: list[dict[str, str]], col_name: str) -> list[str]:
    """Make a list of strings of values in a column."""
    col_data: list[str] = []
    for row in row_list:
        col_data.append((row[col_name]))
    return col_data


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform table into a list of rows."""
    col_dictionary: dict[str, list[str]] = {}
    for column in table:
        for name in column:
            values_list = column_values(table, name)
            col_dictionary[name] = values_list  
    return col_dictionary


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce column-based table with only first couple rows."""
    dictionary: dict[str, list[str]] = {}
    while n >= 0:
        for column in table:
            column_list: list[str] = []
            column_list.append(column)
            dictionary[column] = column_list
            n -= 1
    return dictionary


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Make column-based table with specific subset of original columns."""
    dictionary: dict[str, list[str]] = {}
    for column in col_names:
        dictionary[column] = col_names
    return dictionary


def count(input_list: list[str]) -> dict[str, int]:
    """Count frequencies of data on table."""
    dictionary: dict[str, int] = {}
    for item in dictionary:
        if item in input_list:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary