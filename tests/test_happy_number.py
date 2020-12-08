import pytest
from cracking_practices.happy_number.happy_number import find_happy_number


def test_one():

    expected = True

    actual = find_happy_number(23)

    assert actual == expected, 'Error on test_one.'



def test_two():

    expected = False

    actual = find_happy_number(12)

    assert actual == expected, 'Error on test_two.'



