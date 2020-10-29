import pytest
from cracking_practices.permutation_in_a_str.permutation_in_a_str import (
    find_permutation,
)


def test_one():
    String = "oidbcaf"
    Pattern = "abc"

    expected = True

    actual = find_permutation(String, Pattern)

    assert actual == expected, "Error on test one."


def test_two():
    String = "odicf"
    Pattern = "dc"

    expected = False

    actual = find_permutation(String, Pattern)

    assert actual == expected, "Error on test_two."


def test_three():
    String = "bcdxabcdy"
    Pattern = "bcdyabcdx"

    expected = True

    actual = find_permutation(String, Pattern)

    assert actual == expected, "Error on test_three."


def test_four():
    String = "aaacb"
    Pattern = "abc"

    expected = True

    actual = find_permutation(String, Pattern)

    assert actual == expected, "Error on test_four."
