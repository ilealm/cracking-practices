import pytest
from cracking_practices.minimum_window_sort.minimum_window_sort import shortest_window_sort


def test_one():
    array = [ 1, 2, 5, 3, 7, 10, 9, 12 ]
    expected = 5

    actual = shortest_window_sort(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [ 1, 3, 2, 0, -1, 7, 10 ]
    expected = 5

    actual = shortest_window_sort(array)

    assert actual == expected, 'Error on test_two.'


def test_three():
    array = [ 1, 2, 3 ]
    expected = 0

    actual = shortest_window_sort(array)

    assert actual == expected, 'Error on test_three.'


def test_four():
    array = [ 3, 2, 1 ]
    expected = 3

    actual = shortest_window_sort(array)

    assert actual == expected, 'Error on test_four.'
