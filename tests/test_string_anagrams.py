import pytest

from cracking_practices.string_anagrams.string_anagrams import find_string_anagrams

def test_one():
    String = "ppqp"
    Pattern = "pq"
    expected = [1, 2]

    actual = find_string_anagrams(String, Pattern)

    assert actual == expected, 'Error on test one'

def test_two():
    String = "abbcabc"
    Pattern = "abc"
    expected =  [2, 3, 4]

    actual = find_string_anagrams(String, Pattern)

    assert actual == expected, 'Error on test two.'

