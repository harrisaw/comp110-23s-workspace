"""Ex. 04 - List Utility Functions."""

__author__: str = "730316865"


def all(int_list: list[int], check_int: int) -> bool:
    """Return True if all elements of int_list match check_int."""
    # Establish list_len value and idx for use in loop.
    list_len = len(int_list)
    idx = 0

    # Return False if int_list is empty.
    if list_len == 0:
        return False

    # Loop to check equality of list at index and check_int.
    # If inequality found, return False immediately.
    while idx < list_len:
        if check_int != int_list[idx]:
            return False
        idx += 1

    # If no inequality found in loop, return True.
    return True


def max(int_list: list[int]) -> int:
    """Returns the max value of a list of integers."""
    # Establishing list_len for use in error check and loop below.
    list_len = len(int_list)

    # If int_list is empty, raise a ValueError error.
    if list_len == 0:
        raise ValueError("max() are is an empty List")
    else:
        # Save current max as max, starting with first element in list.
        max = int_list[0]

        # Loop through the list comparing each value to current max.
        # At each iteration, update max if current max is less than current element.
        idx = 1
        while idx < list_len:
            if max < int_list[idx]:
                max = int_list[idx]
            idx += 1

        # Return identified max.
        return max


def is_equal(int_list_a: list[int], int_list_b: list[int]) -> bool:
    """Return True if all values of List A match List B at each index."""
    # Return True if both lists are empty.
    if len(int_list_a) == 0 and len(int_list_b) == 0:
        return True
    # Return False if lists are different lengths.
    elif len(int_list_a) != len(int_list_b):
        return False
    else:
        # Establish list_len and idx for use in loop below.
        list_len = len(int_list_a)
        idx = 0

        # Loop to check equality of List A and List B at each index.
        # Return False immediately if inequality found.
        while idx < list_len:
            if int_list_a[idx] != int_list_b[idx]:
                return False
            idx += 1

    # If no inequality found in loop, return True.
    return True


# python -m exercises.ex04_utils
# python -m tools.submission exercises/ex04_utils.py