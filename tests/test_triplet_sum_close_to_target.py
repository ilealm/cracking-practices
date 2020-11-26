import pytest
from cracking_practices.triplet_sum_close_to_target.triplet_sum_close_to_target import (
    triplet_sum_close_to_target,
)


def test_one():
    array = [-2, 0, 1, 2]
    target = 2

    expected = 1

    actual = triplet_sum_close_to_target(array, target)

    assert actual == expected, "Error on test_one."


def test_two():
    array = [-3, -1, 1, 2]
    target = 1

    expected = 0

    actual = triplet_sum_close_to_target(array, target)

    assert actual == expected, "Error on test_two."


def test_three():
    array = [1, 0, 1, 1]
    target = 100

    expected = 3

    actual = triplet_sum_close_to_target(array, target)

    assert actual == expected, "Error on test_three."

