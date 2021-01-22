import pytest
from cracking_practices.find_smallest_missing_possitive_number.find_smallest_missing_possitive_number import find_first_smallest_missing_positive


def test_one():
    array = [-3, 1, 5, 4, 2]
    expected = 3

    actual = find_first_smallest_missing_positive(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [3, -2, 0, 1, 2]
    expected = 4

    actual = find_first_smallest_missing_positive(array)

    assert actual == expected, 'Error on test_two.'


def test_three():
    array = [3, 2, 5, 1]
    expected = 4

    actual = find_first_smallest_missing_positive(array)

    assert actual == expected, 'Error on test_three.'
