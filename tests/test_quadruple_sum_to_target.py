import pytest
from cracking_practices.quadruple_sum_to_target.quadruple_sum_to_target import search_quadruplets


def test_one():
    array = [4, 1, 2, -1, 1, -3]
    target = 1

    expected = [ [-3, -1, 1, 4], [-3, 1, 1, 2] ]

    actual = search_quadruplets(array, target)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [2, 0, -1, 1, -2, 2]
    target = 2

    expected = [ [-1, 0, 1, 2] , [-2, 0, 2, 2] ]

    actual = search_quadruplets(array, target)

    assert actual == expected, 'Error on test_two.'


