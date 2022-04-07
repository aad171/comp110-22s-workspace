"""Dictionary related utility functions."""

__author__ = "730486473"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data_table: dict[str, list[str]], row_number: int) -> dict[str, list[str]]:
    """Produce specified dataset."""
    final_table: dict[str, list[str]] = {}
    for column in data_table:
        storage: list[str] = []
        column_value = data_table[column]
        i: int = 0
        if row_number > len(column_value):
            row_number = len(column_value)
        while i < row_number:
            storage.append(column_value[i])
            i += 1
        final_table[column] = storage
    return final_table


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a selected dataset."""
    result: dict[str, list[str]] = {}
    for name in column_names:
        result[name] = column_table[name]
    return result
    

def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatenate one dataset with another."""
    result: dict[str, list[str]] = {}
    for column in first_table:
        result[column] = first_table[column]
    for column in second_table:
        if column in result:
            column_list: list[str] = second_table[column]
            for value in column_list:
                result[column].append(value)
        else: 
            result[column] = second_table[column]
    return result
        

def count(values: list[str]) -> dict[str, int]:
    """Find the frequency of the values in the dataset."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def analyze(dataset: dict[str, int], column_name: str) -> str:
    lower_ratings: int = 0
    higher_ratings: int = 0
    for rating in dataset:
        if rating == "1":
            level_one = dataset[rating]
            lower_ratings += level_one
        if rating == "2":
            level_two = dataset[rating]
            lower_ratings += level_two
        if rating == "3":
            level_three = dataset[rating]
            lower_ratings += level_three
        if rating == "4":
            level_four = dataset[rating]
            lower_ratings += level_four
        if rating == "5":
            level_five = dataset[rating]
            higher_ratings += level_five
        if rating == "6":
            level_six = dataset[rating]
            higher_ratings += level_six
        if rating == "7":
            level_seven = dataset[rating]
            higher_ratings += level_seven
    if higher_ratings > lower_ratings:
        difference = (higher_ratings - lower_ratings)
        return f"More people voted higher for {column_name}, there were {difference} more ratings from 5-7 than from 1-4 and there were {higher_ratings + lower_ratings} ratings in total." 
    else:
        difference = lower_ratings - higher_ratings
        return f"More people voted lower for {column_name}, there were {difference} more ratings from 1-4 than 5-7 and there were {higher_ratings + lower_ratings} ratings in total. "