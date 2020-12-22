import pytest
from cracking_practices.insert_interval.insert_interval import insert


def test_one():

    expected = [[1, 3], [4, 7], [8, 12]]

    actual = insert([[1, 3], [5, 7], [8, 12]], [4, 6])

    assert actual == expected, 'Error on test_one.'



def test_two():

    expected = [[1, 3], [4, 12]]

    actual = insert([[1, 3], [5, 7], [8, 12]], [4, 10])

    assert actual == expected, 'Error on test_two.'


def test_three():

    expected = [[1, 4], [5, 7]]

    actual = insert([[2, 3], [5, 7]], [1, 4])

    assert actual == expected, 'Error on test_three.'


