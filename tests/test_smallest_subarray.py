import pytest
from cracking_practices.smallest_subarray.smallest_subarray import smallest_subarray

def test_one():
    array = [2,3,5,2,3,2]
    S = 8
    expected = 2

    actual = smallest_subarray(array, S)

    assert actual == expected, 'Error on test_one.'


def test_two():
    array = [2, 1, 5, 2, 3, 2]
    S = 7
    expected = 2

    actual = smallest_subarray(array, S)

    assert actual == expected, 'Error on test_two'

def test_three():
    array = [3, 4, 1, 1, 6]
    S=8
    expected = 3
    actual = smallest_subarray(array, S)

    assert actual == expected, 'Error on test_three'


def test_four():
    array = [2, 1, 5, 2, 8]
    S = 7
    expected = 1

    actual = smallest_subarray(array, S)

    assert actual == expected, 'Error on test_four'


def test_five():
    array = [2, 1, 5, 2, 3, 2]
    S = 70
    expected = 0

    actual = smallest_subarray(array, S)

    assert actual == expected, 'Error on test_five'
