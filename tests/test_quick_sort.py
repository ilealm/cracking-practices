import pytest
from cracking_practices.quick_sort.quick_sort import quick_sort

def test_one():
    test = [19, 220, 63, 105, 2]
    expected = [2, 19, 63, 105, 220]

    actual = quick_sort(test, 0, len(test)-1)

    assert actual == expected, 'Error on test_one.'


def test_two():
    test =  [10, 15, -3, 12, 1, 30, 7]
    expected = [-3, 1, 7, 10, 12, 15, 30]

    actual = quick_sort(test, 0, len(test)-1)

    assert actual == expected, 'Error on test_two.'
