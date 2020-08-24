import pytest
from cracking_practices.reverse_string.reverse_string import reverse_string

def test_one():
    test = 'bunny'
    expected = 'ynnub'

    actual = reverse_string(test)

    assert actual == expected, 'Error on test_one.'


def test_two():
    test = 'the dog is sleeping'
    expected = 'gnipeels si god eht'

    actual = reverse_string(test)

    assert actual == expected, 'Error on test_two.'


def test_three():
    test = 'a'
    expected = 'a'

    actual = reverse_string(test)

    assert actual == expected, 'Error on test_three.'


def test_four():
    test = 'a '
    expected = ' a'

    actual = reverse_string(test)

    assert actual == expected, 'Error on test_four.'

def test_five():
    test = 'aBcD e'
    expected = 'e DcBa'

    actual = reverse_string(test)

    assert actual == expected, 'Error on test_five.'
