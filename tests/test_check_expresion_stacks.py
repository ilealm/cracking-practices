import pytest
from cracking_practices.check_expresion_stacks.check_expresion_stacks import (
    check_expresion,
)


def test_one():
    exp = "(1+2)"
    expected = True

    actual = check_expresion(exp)

    assert actual == expected, "Error on test_one."


def test_two():
    exp = "1+2)"
    expected = False

    actual = check_expresion(exp)

    assert actual == expected, "Error on test_two."


def test_three():
    exp = "(1+2) <1>"
    expected = True

    actual = check_expresion(exp)

    assert actual == expected, "Error on test_three."


def test_four():
    exp = "(1+2<) 1>"
    expected = False

    actual = check_expresion(exp)

    assert actual == expected, "Error on test_four."


def test_five():
    exp = "(1+2) <1> - {5+9}"
    expected = True

    actual = check_expresion(exp)

    assert actual == expected, "Error on test_five."


def test_six():
    exp = "(1+2)  {5+9 (7)"
    expected = False

    actual = check_expresion(exp)

    assert actual == expected, "Error on test_six."
