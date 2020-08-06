import pytest
from cracking_practices.run_length_encoding.run_length_encoding import run_length_encoding


def test_run_length_encoding_one():
    expected = '3b2c4a1a'

    actual = run_length_encoding('aaabbcccca')

    assert actual == expected, "Error on test_run_length_encoding_one."


def test_run_length_encoding_two():
    expected = '8a'

    actual = run_length_encoding('aaaaaaaa')

    assert actual == expected, "Error on test_run_length_encoding_two."


def test_run_length_encoding_three():
    expected = '1b1c1d1e1e'

    actual = run_length_encoding('abcde')

    assert actual == expected, "Error on test_run_length_encoding_three."


def test_run_length_encoding_four():
    expected = '1a'

    actual = run_length_encoding('a')

    assert actual == expected, "Error on test_run_length_encoding_four."


def test_run_length_encoding_five():
    expected = '3515'

    actual = run_length_encoding('1115')

    assert actual == expected, "Error on test_run_length_encoding_one."



