import pytest
from cracking_practices.selection_sort.selection_sort import selection_sort


def test_selection_six_items():
    array = [20, 9, 25, 6, 30, 1]
    expected = [1, 6, 9, 20, 25, 30]

    actual = selection_sort(array)

    assert actual == expected, 'Error on test_selection_six_items.'


def test_selection_three_items():
    array = [10, 30, 25]
    expected = [10, 25, 30]

    actual = selection_sort(array)

    assert actual == expected, 'Error on test_selection_three_items.'


def test_empty_list():
    array = []
    expected = []

    actual = selection_sort(array)

    assert actual == expected, 'Error on test_empty_list.'



def test_duplicated_intems():
    array = [ 45, 30, 5, 45, 6, 30, 25]
    expected = [5, 6, 25, 30, 30, 45, 45]

    actual = selection_sort(array)

    assert actual == expected, 'Error on test_duplicated_intems.'



def test_letters():
    array = [ 'b', 'e', 'c', 'a', 'd']
    expected = [ 'a', 'b', 'c', 'd', 'e']

    actual = selection_sort(array)

    assert actual == expected, 'Error on test_letters.'
