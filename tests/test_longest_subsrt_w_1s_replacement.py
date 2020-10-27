import pytest
from cracking_practices.longest_subsrt_w_1s_replacement.longest_subsrt_w_1s_replacement import length_of_longest_substring

def test_one():
    Array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k = 2
    expected = 6

    actual = length_of_longest_substring(Array, k)

    assert actual == expected, 'Error on test one.'

def test_two():
    Array = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3
    expected = 9

    actual = length_of_longest_substring(Array, k)

    assert actual == expected, 'Error on test two.'


