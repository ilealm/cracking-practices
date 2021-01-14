import pytest
from cracking_practices.find_all_missing_numbers.find_all_missing_numbers import find_missing_numbers


def test_one():
    array = [2, 3, 1, 8, 2, 3, 5, 1]
    expected = [4, 6, 7]

    actual = find_missing_numbers(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [2, 4, 1, 2]
    expected = [3]

    actual = find_missing_numbers(array)

    assert actual == expected, 'Error on test_two.'


def test_three():
    array = [2, 3, 2, 1]
    expected = [4]

    actual = find_missing_numbers(array)

    assert actual == expected, 'Error on test_three.'
