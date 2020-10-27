import pytest
from cracking_practices.longest_subsrt_w_replacement.longest_subsrt_w_replacement import longest_subsrt_w_replacement

def test_one():
    String="aabccbb"
    k = 2

    expected =  5 #'bbbbb'

    actual = longest_subsrt_w_replacement(String, k)

    assert actual == expected, 'Error on test_one.'


def test_two():
    String="abbcb"
    k = 1

    expected = 4 # 'bbbb'

    actual = longest_subsrt_w_replacement(String, k)

    assert actual == expected, 'Error on test_two.'


def test_three():
    String="abccde"

    k = 1

    expected = 3 # 'ccc'

    actual = longest_subsrt_w_replacement(String, k)

    assert actual == expected, 'Error on test_three.'
