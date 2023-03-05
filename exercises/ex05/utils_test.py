"""Ex. 05 - List Utility Functions Testing."""

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

__author__: str = "730316865"


# Tests for only_evens.
def test_only_evens_empty() -> None:
    """Edge Case: only_evens test with empty input."""
    assert only_evens([]) == []


def test_only_evens_many() -> None:
    """Use Case: only_evens test with many evens in input."""
    assert only_evens([0, 1, 2, 3]) == [0, 2]


def test_only_evens_none() -> None:
    """Use Case: only_evens test with no evens in input."""
    assert only_evens([1, 3, 5]) == []


# Tests for sub.
def test_sub_empty_range() -> None:
    """Edge Case: sub test with same start and end index."""
    # Edge case (index range == 0).
    assert sub([0, 1, 2], 1, 1) == []


def test_sub_inside_bounds() -> None:
    """Use Case: sub test with start and end inside index range of input."""
    assert sub([0, 1, 2], 0, 2) == [0, 1, 2]


def test_sub_outside_bounds() -> None:
    """Use Case: sub test with start and end outside index range of input."""
    assert sub([0, 1, 2], -1, 3) == [0, 1, 2]


# Tests for concat.
def test_concat_empty() -> None:
    """Edge Case: concat test with two empty inputs."""
    assert concat([], []) == []


def test_concat_one_empty() -> None:
    """Use Case: concat test with one empty input."""
    assert concat([1, 2], []) == [1, 2]


def test_concat_neither_empty() -> None:
    """Use Case: concat test with np empty inputs."""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]