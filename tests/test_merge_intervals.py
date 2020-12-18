import pytest
from cracking_practices.merge_intervals.merge_intervals import merge, Interval


def test_one():
    expected = [[1,5], [7,9]]

    actual = merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)])

    assert actual == expected, 'Error on test_one.'



def test_two():

    expected = [ [5, 9], [2, 4] ]

    actual = merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)])

    assert actual == expected, 'Error on test_two.'


def test_three():

    expected = [[1,6]]

    actual = merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)])

    assert actual == expected, 'Error on test_three.'
