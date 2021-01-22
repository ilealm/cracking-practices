import pytest
from cracking_practices.find_the_corrupt_pair.find_the_corrupt_pair import find_corrupt_numbers


def test_one():
    array = [3, 1, 2, 5, 2]
    expected = [2, 4]

    actual = find_corrupt_numbers(array)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array =  [3, 1, 2, 3, 6, 4]
    expected = [3, 5]

    actual = find_corrupt_numbers(array)

    assert actual == expected, 'Error on test_two.'


