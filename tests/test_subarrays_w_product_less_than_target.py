import pytest
from cracking_practices.subarrays_w_product_less_than_target.subarrays_w_product_less_than_target import find_subarrays


def test_one():
    array = [2, 5, 3, 10]
    target = 30

    expected = [[2], [5], [2, 5], [3], [5, 3], [10]]

    actual = find_subarrays(array, target)

    assert actual == expected, 'Error on test_one.'


def test_two():
    array = [8, 2, 6, 5]
    target = 50

    expected = [ [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] ]

    actual = find_subarrays(array, target)

    assert actual == expected, 'Error on test_two.'

