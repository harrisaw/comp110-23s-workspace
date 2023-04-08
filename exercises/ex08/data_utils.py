"""Ex. 08 - Data Utils."""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as list of dicts with header key."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    # Step through table.
    for row in table:
        # Save every value under key "header".
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers."""
    result: dict[str, list[str]] = {}
    # Loop through keys of one row of table.
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # For each key, make a dictionary entry with all column values.
        result[key] = column_values(table, key)
    return result


def head(input: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns dictionary with column headers with specified number of rows."""
    result: dict[str, list[str]] = {}
    # Loop through each header.
    for header in input:
        input_values = input[header]

        if len(input_values) < rows:
            max_rows = len(input_values)
        else:
            max_rows = rows
        
        head_values = []
        idx = 0
        while idx < max_rows:
            head_values.append(input_values[idx])
            idx += 1
        result[header] = head_values
    return result


def select(input: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Returns dictionary with specified column headers."""
    result: dict[str, list[str]] = {}
    # Loop through each header in input list and copy results if in list.
    for c in columns:
        result[c] = input[c]
    return result
    

def concat(input_1: dict[str, list[str]], input_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two dictionary of lists."""
    result: dict[str, list[str]] = {}
    # Loop through columns in first input.
    for col in input_1:
        values = input_1[col]
        if col in input_2:
            for i in input_2[col]:
                values.append(i)
        result[col] = values
    # Loop through columns in second input.
    for col in input_2:
        if col not in result:
            result[col] = input_2[col]
    return result


def count(input: list[str]) -> dict[str, int]:
    """Returns dictionary with counts of occurences of str in list."""
    result: dict[str, int] = {}
    # Loop through input list.
    for i in input:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


# python -m tools.submission exercises/ex08