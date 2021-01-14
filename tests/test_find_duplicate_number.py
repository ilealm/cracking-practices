import pytest
from cracking_practices.find_duplicate_number.find_duplicate_number import find_duplicate


def test_one():
    array = [1, 4, 4, 3, 2]
    expected = 4

    actual = find_duplicate(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [2, 1, 3, 3, 5, 4]
    expected = 3

    actual = find_duplicate(array)

    assert actual == expected, 'Error on test_two.'


def test_three():
    array = [2, 4, 1, 4, 4]
    expected = 4

    actual = find_duplicate(array)

    assert actual == expected, 'Error on test_three.'
