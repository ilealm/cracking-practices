import pytest
from cracking_practices.maximum_cpu_load.maximum_cpu_load import job, find_max_cpu_load


def test_one():
    expected = 7

    actual = find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])

    assert actual == expected, 'Error on test_one.'



def test_two():
    expected = 15

    actual = find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])

    assert actual == expected, 'Error on test_two.'


def test_three():
    expected = 8

    actual = find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])

    assert actual == expected, 'Error on test_three.'
