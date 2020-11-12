import pytest
from cracking_practices.words_concatenation.words_concatenation import find_word_concatenation

def test_one():
    String = "catfoxcat"
    Words = ["cat", "fox"]

    expected = [0, 3]

    actual = find_word_concatenation(String, Words)

    assert actual == expected, 'Error on test_one'


def test_two():
    String = "catcatfoxfox"
    Words = ["cat", "fox"]

    expected = [3]

    actual = find_word_concatenation(String, Words)

    assert actual == expected, 'Error on test_two'
