import pytest
from cracking_practices.dutch_national_flag.dutch_national_flag import dutch_flag_sort


def test_one():
    array = [1, 0, 2, 1, 0]

    expected = [0, 0, 1, 1, 2]

    actual = dutch_flag_sort(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [2, 2, 0, 1, 2, 0]

    expected = [0, 0, 1, 2, 2, 2 ]

    actual = dutch_flag_sort(array)

    assert actual == expected, 'Error on test_two.'



