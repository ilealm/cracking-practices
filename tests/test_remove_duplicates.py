import pytest
from cracking_practices.remove_duplicates.remove_duplicates import remove_duplicates

def test_one():
    arr = [2, 3, 3, 3, 6, 9, 9]

    expected = 4

    actual = remove_duplicates(arr)

    assert actual == expected, 'Error on test_one.'


def test_two():
    arr = [2, 2, 2, 11]

    expected = 2

    actual = remove_duplicates(arr)

    assert actual == expected, 'Error on test_two.'
