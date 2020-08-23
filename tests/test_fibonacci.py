import pytest
from cracking_practices.fibonacci.fibonacci import fibonacci

def test_one():
    expected = 1
    which_fibonacci = 1

    actual = fibonacci(which_fibonacci)

    assert actual == expected, 'Error on test_one.'

def test_two():
    which_fibonacci = 2
    expected = 1

    actual = fibonacci(which_fibonacci)

    assert actual == expected, 'Error on test_two.'


def test_five():
    which_fibonacci = 5
    expected = 5

    actual = fibonacci(which_fibonacci)

    assert actual == expected, 'Error on test_five.'


def test_ten():
    which_fibonacci = 10
    expected = 55

    actual = fibonacci(which_fibonacci)

    assert actual == expected, 'Error on test_ten.'

def test_fifthteen():
    which_fibonacci = 15
    expected = 610

    actual = fibonacci(which_fibonacci)

    assert actual == expected, 'Error on test_fifthteen.'


def test_twenty():
    which_fibonacci = 20
    expected = 6765

    actual = fibonacci(which_fibonacci)

    assert actual == expected, 'Error on test_twenty.'

