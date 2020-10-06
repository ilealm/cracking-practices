import pytest
from cracking_practices.longest_substring.longest_substring import longest_substring

def test_one():
    letters = "araaci"
    K = 2
    expected = 4

    actual = longest_substring(letters, K)

    assert actual == expected, 'Error on test_one'


def test_two():
    letters = "araaci"
    K = 1
    expected = 2

    actual = longest_substring(letters, K)

    assert actual == expected, 'Error on test_two'


def test_three():
    letters = "cbbebi"
    K = 3
    expected = 5

    actual = longest_substring(letters, K)

    assert actual == expected, 'Error on test_three'
