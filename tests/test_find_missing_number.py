import pytest
from cracking_practices.find_missing_number.find_missing_number import (
    find_missing_number,
)


def test_one():
    array = [4, 0, 3, 1]
    expected = 2

    actual = find_missing_number(array)

    assert actual == expected, "Error on test_one."


def test_two():
    array = [8, 3, 5, 2, 4, 6, 0, 1]
    expected = 7

    actual = find_missing_number(array)

    assert actual == expected, "Error on test_two."

