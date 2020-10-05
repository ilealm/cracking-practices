import pytest
from cracking_practices.average_subarrays.average_subarrays import average_subarrays

def test_one():
    expected = []

    array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    K = 10

    actual = average_subarrays(array, K)

    assert actual ==  expected, 'Error on test_one.'


def test_two():
    expected = [2.2, 2.8, 2.4, 3.6, 2.8]

    array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    K = 5

    actual = average_subarrays(array, K)

    assert actual ==  expected, 'Error on test_two.'



def test_tree():
    expected = [15, 25, 35, 45]

    array = [10,20,30,40,50]
    K = 2

    actual = average_subarrays(array, K)

    assert actual ==  expected, 'Error on test_tree.'



def test_four():
    expected = [10, 10, 10, 10]

    array = [10,10,10,10,10]
    K = 2

    actual = average_subarrays(array, K)

    assert actual ==  expected, 'Error on test_four.'
