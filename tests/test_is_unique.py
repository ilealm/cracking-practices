import pytest
from cracking_practices.is_unique.is_unique import is_unique

def test_is_unique_one():
    word = 'abcde'
    expected = True

    actual = is_unique(word)

    assert actual == expected, "Error on is_unique_one."

def test_is_unique_two():
    word = 'abcdea'
    expected = False

    actual = is_unique(word)

    assert actual == expected, "Error on test_is_unique_two."

def test_is_unique_three():
    word = 'abcde a 125'
    expected = False

    actual = is_unique(word)

    assert actual == expected, "Error on test_is_unique_three."


def test_is_unique_four():
    word = 'bear & dog'
    expected = False

    actual = is_unique(word)

    assert actual == expected, "Error on test_is_unique_four."

def test_is_unique_five():
    word = '0123456789'
    expected = True

    actual = is_unique(word)

    assert actual == expected, "Error on test_is_unique_five."


def test_is_unique_six():
    word = '0123456789 10'
    expected = False

    actual = is_unique(word)

    assert actual == expected, "Error on test_is_unique_six."

def test_is_unique_seven():
    word = ''
    expected = False

    actual = is_unique(word)

    assert actual == expected, "Error on test_is_unique_seven."
