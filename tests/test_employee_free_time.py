import pytest
from cracking_practices.employee_free_time.employee_free_time import Interval, find_employee_free_time


def test_one():
    input = [[Interval(1, 3), Interval(5, 6)], [
            Interval(2, 3), Interval(6, 8)]]
    expected =[3,5]

    actual = find_employee_free_time(input)

    assert actual == expected, 'Error on test_one.'



def test_two():
    input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4), Interval(6, 8)]]
    expected = [4,6], [8,9]

    actual = find_employee_free_time(input)

    assert actual == expected, 'Error on test_two.'


def test_three():
    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    expected = [5,7]

    actual = find_employee_free_time(input)

    assert actual == expected, 'Error on test_three.'
