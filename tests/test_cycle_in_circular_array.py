import pytest
from cracking_practices.cycle_in_circular_array.cycle_in_circular_array import circular_array_loop_exists


def test_one():
    array = [1, 2, -1, 2, 2]
    expected = True

    actual = circular_array_loop_exists(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [2, 2, -1, 2]
    expected = True

    actual = circular_array_loop_exists(array)

    assert actual == expected, 'Error on test_two.'


def test_three():
    array = [2, 1, -1, -2]
    expected = False

    actual = circular_array_loop_exists(array)

    assert actual == expected, 'Error on test_three.'
