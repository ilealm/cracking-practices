import pytest
from cracking_practices.triplets_with_smaller_sum.triplets_with_smaller_sum import triplet_with_smaller_sum

def test_one():
    array = [-1, 0, 2, 3]
    target = 3

    expected = 2

    actual = triplet_with_smaller_sum(array,target)

    assert actual ==  expected, 'Error on test_one.'


def test_two():
    array = [-1, 4, 2, 1, 3]
    target = 5

    expected = 4

    actual = triplet_with_smaller_sum(array,target)

    assert actual ==  expected, 'Error on test_two.'


