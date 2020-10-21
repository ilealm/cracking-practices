import pytest
from cracking_practices.no_repeat_substring.no_repeat_substring import no_repeat_substring

def test_one():
    word = "aabccbb"
    expected = 3

    actual = no_repeat_substring(word)

    assert actual == expected, 'Error on test_one.'


def test_two():
    word = "abbbb"
    expected = 2

    actual = no_repeat_substring(word)

    assert actual == expected, 'Error on test_two.'



def test_three():
    word = "abccde"
    expected = 3

    actual = no_repeat_substring(word)

    assert actual == expected, 'Error on test_three.'
