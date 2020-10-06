import pytest
from cracking_practices.max_sub_array.max_sub_array import max_sub_array

def test_one():
    array = [5, 10, 5, 21, 13, 5, 100]
    K = 20
    expected = -1

    actual = max_sub_array(array, K)

    assert actual == expected, 'Error on test one.'


def test_two():
    array = [5, 10, 5, 21, 13, 5, 100]
    K = 3
    expected = 118

    actual = max_sub_array(array, K)

    assert actual == expected, 'Error on test two.'


def test_three():
    array =[2, 3, 40, 10, 5]
    K = 2
    expected = 50

    actual = max_sub_array(array, K)

    assert actual == expected, 'Error on test three.'


def test_four():
    array =  [2, 1, 5, 1, 3, 2]
    K = 3
    expected = 9

    actual = max_sub_array(array, K)

    assert actual == expected, 'Error on test_four.'


def test_five():
    array =[2, 3, 4, 1, 5]
    K = 2
    expected = 7

    actual = max_sub_array(array, K)

    assert actual == expected, 'Error on test_five.'


def test_six():
    array =[]
    K = 2
    expected = -1

    actual = max_sub_array(array, K)

    assert actual == expected, 'Error on test_five.'
