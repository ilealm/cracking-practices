import pytest
from cracking_practices.string_rotation.string_rotation import string_rotation


def test_string_rotation_one():
    original_str = "waterbottle"
    lookup_str = ""

    expected = False

    actual = string_rotation(original_str, lookup_str)

    assert actual == expected, "Error on test_string_rotation_one."


def test_string_rotation_two():
    original_str = "waterbottle"
    lookup_str = "erbottlewat"

    expected = True

    actual = string_rotation(original_str, lookup_str)

    assert actual == expected, "Error on test_string_rotation_two."


def test_string_rotation_three():
    original_str = "waterBottlE"
    lookup_str = "erbottlewat"

    expected = True

    actual = string_rotation(original_str, lookup_str)

    assert actual == expected, "Error on test_string_rotation_three."


def test_string_rotation_four():
    original_str = "rainbow"
    lookup_str = "bowrain"

    expected = True

    actual = string_rotation(original_str, lookup_str)

    assert actual == expected, "Error on test_string_rotation_four."


def test_string_rotation_five():
    original_str = "abcde"
    lookup_str = "abcde"

    expected = True

    actual = string_rotation(original_str, lookup_str)

    assert actual == expected, "Error on test_string_rotation_five."


def test_string_rotation_six():
    original_str = "abcdefg"
    lookup_str = "efgcde"

    expected = False

    actual = string_rotation(original_str, lookup_str)

    assert actual == expected, "Error on test_string_rotation_six."


def test_string_rotation_seven():
    original_str = "rainbow"
    lookup_str = "rain"

    expected = False

    actual = string_rotation(original_str, lookup_str)

    assert actual == expected, "Error on test_string_rotation_seven."


def test_string_rotation_eight():
    original_str = "rainbow"
    lookup_str = "wrainbo"

    expected = True

    actual = string_rotation(original_str, lookup_str)

    assert actual == expected, "Error on test_string_rotation_eight."
