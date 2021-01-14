import pytest
from cracking_practices.find_all_duplicate_numbers.find_all_duplicate_numbers import find_all_duplicates


def test_one():
    array = [3, 4, 4, 5, 5]

    expected = [4, 5]

    actual = find_all_duplicates(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [5, 4, 7, 2, 3, 5, 3]
    expected = [3, 5]

    actual = find_all_duplicates(array)

    assert actual == expected, 'Error on test_two.'
