"""EX07: Dictionary Utils."""

__author__: str = "730316865"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    output_dict: dict[str, str] = {}
    # Looping through each key of input_dict as the new_value.
    for new_value in input_dict:
        # Taking value of input_dict as new_key.
        new_key = input_dict[new_value]
        if new_key in output_dict:
            raise KeyError("Same key appears twice.")
        # Assigning new_key and new_value as entry in output_dict.
        output_dict[new_key] = new_value
    # Returning inverted dictionary.
    return output_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the most common value in the dictionary."""
    # Initiates a list of every value in the dictionary.
    values = list(input_dict.values())

    # Initiates an empty dictionary to keep track of value counts.
    count_dict: dict[str, int] = {}

    # Loops through each of the values (colors).
    for color in values:
        idx = 0
        count = 0
        # Loops through value list and counts the number of matches.
        while idx < len(values):
            if values[idx] == color:
                count += 1
            idx += 1
        # Saves color with the count in the value list.
        count_dict[color] = count

    # Initiates empty string for output and highest count at 0.
    favorite_color: str = None
    highest_count = 0

    # Loops through each value on value list.
    for color in values:
        # If color is not current favorite color, compares count in dictionary.
        if favorite_color is None:
            favorite_color = color
            highest_count = count_dict[color]
        elif color != favorite_color:
            if count_dict[color] > highest_count:
                favorite_color = color
                highest_count = count_dict[color]
                # Save new favorite color and count if count is higher.
    
    # Returning favorite color.
    return favorite_color
 

def count(input_list: list[str]) -> dict[str, int]:
    """Returns dictionary with count of elements in list."""
    # Initiating empty output dict.
    output_dict: dict[str, int] = {}
    # Looping through list elements.
    for x in input_list:
        # If x is in the dictionary, increase count by 1. Otherwise add to dictionary.
        if x in output_dict:
            output_dict[x] += 1
        else:
            output_dict[x] = 1
    # Return finished dictionary.
    return output_dict


# python -m tools.submission exercises/ex07
# python -m exercises.ex07.dictionary