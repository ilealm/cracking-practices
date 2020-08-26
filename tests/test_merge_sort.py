import pytest
from cracking_practices.merge_sort.merge_sort import merge_sort

def test_one():
    test = [30, 25, 15, 41, 5, 80, 40, 1]
    expected = [1, 5, 15, 25, 30, 40, 41, 80]

    actual = merge_sort(test)

    assert actual == expected, 'Error on test_one.'


def test_two():
    test = [50, 100]
    expected = [50 , 100]

    actual = merge_sort(test)

    assert actual == expected, 'Error on test_two.'


def test_three():
    test = [100, 90,80,70,60,10]
    expected = [10, 60, 70, 80, 90, 100]

    actual = merge_sort(test)

    assert actual == expected, 'Error on test_three.'

def test_four():
    test = [1, 1, 1, 1]
    expected = [1, 1, 1, 1]

    actual = merge_sort(test)

    assert actual == expected, 'Error on test_four.'

def test_five():
    test = []
    expected = []

    actual = merge_sort(test)

    assert actual == expected, 'Error on test_five.'


def test_six():
    test = [ 50, 200, 30, 65, 98, 10, 45]
    expected = [ 10, 30, 45, 50, 65, 98, 200 ]

    actual = merge_sort(test)

    assert actual == expected, 'Error on test_one.'
