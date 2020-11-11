import pytest
from cracking_practices.smallest_containing_substrig.smallest_containing_substrig import find_substring

def test_one():
    String = "aabdec"
    Pattern = "abc"

    expected = "abdec"

    actual = find_substring(String, Pattern)

    assert actual ==  expected, 'Error on test one.'

def test_two():
    String = "abdbca"
    Pattern = "abc"

    expected = "bca"

    actual = find_substring(String, Pattern)

    assert actual ==  expected, 'Error on test two.'



def test_tree():
    String = "adcad"
    Pattern = "abc"

    expected = ""

    actual = find_substring(String, Pattern)

    assert actual ==  expected, 'Error on test tree.'


def test_four():
    String = "abdabca"
    Pattern = "abc"

    expected = "abc"

    actual = find_substring(String, Pattern)

    assert actual ==  expected, 'Error on test four.'
