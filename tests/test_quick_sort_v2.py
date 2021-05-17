import pytest
from cracking_practices.quick_sort_v2.quick_sort_v2 import quick_sort


def test_seven_elements():
    array = [25, 50, 15, 6, 35, 1, 27]
    expected = [1, 6, 15, 25, 27, 35, 50]

    actual = quick_sort(array)

    assert actual == expected, 'Error on test_seven_elements.'


def test_one_element():
    array = [20]
    expected = [20]

    actual = quick_sort(array)

    assert actual == expected, 'Error on test_one_element.'



def test_empty_array():
    array = []
    expected = []

    actual = quick_sort(array)

    assert actual == expected, 'Error on test_empty_array.'


def test_three_elements():
    array = [36, 20, 6]
    expected = [6, 20, 36]

    actual = quick_sort(array)

    assert actual == expected, 'Error on test_three_elements.'



def test_eleven_elements():
    array = [40, 15, 20, 45, 5, 50, 55, 35, 10, 25, 30 ]
    expected = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

    actual = quick_sort(array)

    assert actual == expected, 'Error on test_eleven_elements.'



def test_letters():
    array = ['b', 'c', 'a','d', 'e']
    expected = ['a', 'b', 'c','d', 'e']

    actual = quick_sort(array)

    assert actual == expected, 'Error on test_letters.'
