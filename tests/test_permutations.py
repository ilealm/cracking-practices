import pytest
from cracking_practices.permutations.permutations import permutations


def test_one():
    expected = 24
    array = ["a", "b", "c", "e"]

    actual = len(permutations(array))

    assert actual == expected, "Error on test_one."


def test_two():
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    array = [1, 2, 3]

    actual = permutations(array)

    assert actual == expected, "Error on test_two."

def test_tree():
    expected = [['a', 'b', 'c', 'e'], ['a', 'b', 'e', 'c'], ['a', 'c', 'b', 'e'], ['a', 'c', 'e', 'b'], ['a', 'e', 'b', 'c'], ['a', 'e', 'c', 'b'], ['b', 'a', 'c', 'e'], ['b', 'a', 'e', 'c'], ['b', 'c', 'a', 'e'], ['b', 'c', 'e', 'a'], ['b', 'e', 'a', 'c'], ['b', 'e', 'c', 'a'], ['c', 'a', 'b', 'e'], ['c', 'a', 'e', 'b'], ['c', 'b', 'a', 'e'], ['c', 'b', 'e', 'a'], ['c', 'e', 'a', 'b'], ['c', 'e', 'b', 'a'], ['e', 'a', 'b', 'c'], ['e', 'a', 'c', 'b'], ['e', 'b', 'a', 'c'], ['e', 'b', 'c', 'a'], ['e', 'c', 'a', 'b'], ['e', 'c', 'b', 'a']]

    array = ["a", "b", "c", "e"]

    actual = permutations(array)

    assert actual == expected, "Error on test_tree."


def test_four():
    array = [1, 2, 3]

    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    actual = permutations(array)

    assert actual == expected, "Error on test_four."
