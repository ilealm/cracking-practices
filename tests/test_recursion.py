import pytest
from cracking_practices.recursion.recursion import (
    recursion_sum,
    recursion_num_items,
    recursion_find_max,
    recursion_binary_search
)


def test_recursion_sum_one():
    array = list(range(1, 7))
    expected = 21

    actual = recursion_sum(array)

    assert actual == expected, "Error on test_recursion_sum_one."


def test_recursion_sum_two():
    array = list(range(1, 100, 10))
    expected = 460

    actual = recursion_sum(array)

    assert actual == expected, "Error on test_recursion_sum_two."


def test_recursion_num_items_one():
    array = list(range(1, 11))
    expected = 10

    actual = recursion_num_items(array)

    assert actual == expected, "Error on test_recursion_num_items_one."


def test_recursion_num_items_two():
    array = list(range(1, 101))
    expected = 100

    actual = recursion_num_items(array)

    assert actual == expected, "Error on test_recursion_num_items_two."


def test_recursion_num_items_two():
    array = []
    expected = 0

    actual = recursion_num_items(array)

    assert actual == expected, "Error on test_recursion_num_items_two."


def test_recursion_find_max_one():
    array = [10, 5, 20, 35, 7, 1]
    expected = 35

    actual = recursion_find_max(array)

    assert actual == expected, "Error on test_recursion_find_max_one."


def test_recursion_find_max_two():
    array = [100, 3 , 250, 6.8, 87, 50]
    expected = 250

    actual = recursion_find_max(array)

    assert actual == expected, "Error on test_recursion_find_max_two."


def test_recursion_binary_search_one():
    array = list(range(5,85,5))
    target = 90
    expected = -1

    actual = recursion_binary_search(array, target)

    assert actual == expected, "Error on test_recursion_binary_search_one."


def test_recursion_binary_search_two():
    array = list(range(5,85,5))
    target = 65
    expected = 65

    actual = recursion_binary_search(array, target)

    assert actual == expected, "Error on test_recursion_binary_search_two."
