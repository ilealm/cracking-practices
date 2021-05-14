import pytest
from cracking_practices.binary_search.binary_search import binary_search


def test_binary_search_one():
    array = list(range(0,50,5))
    value_to_find = 30
    expected = 6

    actual = binary_search(array, value_to_find)

    assert actual == expected, 'Error on test_binary_search_one.'



def test_first_value():
    array = list(range(10,110,10))
    value_to_find = 10
    expected = 0

    actual = binary_search(array, value_to_find)


    assert actual == expected, 'Error on test_first_value.'



def test_last_value():
    array = list(range(0,100,7))
    value_to_find = 98
    expected = 14

    actual = binary_search(array, value_to_find)


    assert actual == expected, 'Error on test_last_value.'


def test_inexistent_value():
    array = list(range(0,100,7))
    value_to_find = 30
    expected = -1

    actual = binary_search(array, value_to_find)


    assert actual == expected, 'Error on test_inexistent_value.'


def test_letters():
    array = ['a','b','c','d','e','f','g']
    value_to_find = 'e'
    expected = 4

    actual = binary_search(array, value_to_find)


    assert actual == expected, 'Error on test_letters.'
