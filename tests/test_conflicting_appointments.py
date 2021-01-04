import pytest
from cracking_practices.conflicting_appointments.conflicting_appointments import can_attend_all_appointments


def test_one():
    array = [[1,4], [2,5], [7,9]]

    expected = False

    actual = can_attend_all_appointments(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [[6,7], [2,4], [8,12]]

    expected = True

    actual = can_attend_all_appointments(array)

    assert actual == expected, 'Error on test_two.'


def test_three():
    array = [[4,5], [2,3], [3,6]]

    expected = False

    actual = can_attend_all_appointments(array)

    assert actual == expected, 'Error on test_three.'
