import pytest
from cracking_practices.triplet_sum_to_zero.triplet_sum_to_zero import search_triplets


def test_one():
    array = [-3, 0, 1, 2, -1, 1, -2]
    expected = [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    # [[-3, 1, 2], [-1, 0, 1], [-2, 0, 2], [-2, 1, 1]]
    #  [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]

    actual = search_triplets(array)

    assert actual == expected, 'Error on test_one'

def test_two():
    array = [-5, 2, -1, -2, 3]
    expected = [[-5, 2, 3], [-2, -1, 3]]

    actual = search_triplets(array)

    assert actual == expected, 'Error on test_two'


