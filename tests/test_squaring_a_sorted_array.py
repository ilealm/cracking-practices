import pytest
from cracking_practices.squaring_a_sorted_array.squaring_a_sorted_array import make_squares


def test_one():
    array = [-2, -1, 0, 2, 3]
    expected = [0, 1, 4, 4, 9]

    actual = make_squares(array)

    assert actual == expected, 'Error on test_one.'


def test_two():
    array = [-3, -1, 0, 1, 2]
    expected = [0, 1, 1, 4, 9]

    actual = make_squares(array)

    assert actual == expected, 'Error on test_two.'

