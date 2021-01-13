import pytest
from cracking_practices.cyclic_sort.cyclic_sort import cyclic_sort


def test_one():
    array = [3, 1, 5, 4, 2]

    expected = [1, 2, 3, 4, 5]

    actual = cyclic_sort(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [2, 6, 4, 3, 1, 5]

    expected = [1, 2, 3, 4, 5, 6]

    actual = cyclic_sort(array)

    assert actual == expected, 'Error on test_two.'


def test_three():
    array = [1, 5, 6, 4, 3, 2]

    expected = [1, 2, 3, 4, 5, 6]

    actual = cyclic_sort(array)

    assert actual == expected, 'Error on test_three.'
