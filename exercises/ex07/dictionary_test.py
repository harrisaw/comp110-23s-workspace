"""EX07: Dictionary Utils - Tests."""

__author__: str = "730316865"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_empty() -> None:
    """Edge Case: Inverting an empty dictionary."""
    assert invert({}) == {}


def test_invert_one() -> None:
    """Use Case: Inverting a dictionary with one element."""
    assert invert({"cat": "dog"}) == {"dog": "cat"}


def test_invert_many() -> None:
    """Use Case: Inverting a dictionary with one element."""
    assert invert({"cat": "dog", "hello": "world", "bingo": "bongo"}) == {"dog": "cat", "world": "hello", "bongo": "bingo"}


def test_favorite_color_empty() -> None:
    """Edge Case: Return None if input dict is empty."""
    assert favorite_color({}) is None


def test_favorite_color_no_ties() -> None:
    """Use Case: Return most common value, with no ties."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_ties() -> None:
    """Use Case: Return most common value, or first of tied values to break tie."""
    assert favorite_color({"Andrew": "green", "Suzy": "yellow", "Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "yellow"


def test_count_empty() -> None:
    """Edge Case: Return empty dict if input dict is empty."""
    assert count({}) == {}


def test_count_no_repeats() -> None:
    """Use Case: Return count dict when no values are repeated."""
    assert count({"cat", "hello", "bingo"}) == {"cat": 1, "hello": 1, "bingo": 1}


def test_count_repeats() -> None:
    """Edge Case: Return count dict when values are repeated."""
    assert count(["bingo", "hello", "cat", "cat", "cat", "hello", "bingo"]) == {"cat": 3, "hello": 2, "bingo": 2}


# python -m pytest exercises/ex07