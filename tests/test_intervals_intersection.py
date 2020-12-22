import pytest
from cracking_practices.intervals_intersection.intervals_intersection import merge


def test_one():

    expected = [[2, 3], [5, 6], [7, 7]]

    actual = merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])

    assert actual == expected, 'Error on test_one.'



def test_two():

    expected = [[5, 7], [9, 10]]

    actual = merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])

    assert actual == expected, 'Error on test_two.'


