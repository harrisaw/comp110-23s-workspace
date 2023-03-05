"""Ex. 05 - List Utility Functions."""

__author__: str = "730316865"


def only_evens(input_list: list[int]) -> list[int]:
    """Returns only even elements of a list."""
    # Establish output list.
    output_list: list[int] = []
    # Loop through elements of input_list, adding even (% 2 == 0) elements to output_list.
    for i in input_list:
        if i % 2 == 0:
            output_list.append(i)
    # Return output list.
    return output_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Returns elements of list 2 appended onto list 1."""
    # Establish output list.
    output_list = []
    # Use for loop to append elements of list_1 onto the output list.
    for i in list_1:
        output_list.append(i)
    # Use for loop to append elements of list_1 onto the output list.
    for j in list_2:
        output_list.append(j)
    # Return output list.
    return output_list


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a subset on input list based from start index up to end index."""
    # Establish output list.
    output_list = []
    # If start_index input is negative, replace with 0.
    if start_index < 0:
        start_index = 0
    # If end_index is greater than length of input list, replace with list length.
    if end_index > len(input_list):
        end_index = len(input_list)
    # Starting loop index at start index.
    # Appending elements at correct index range to output list.
    idx = start_index
    while idx < end_index:
        output_list.append(input_list[idx])
        idx += 1
    # Return output list.
    return output_list