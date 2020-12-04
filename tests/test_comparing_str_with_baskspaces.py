import pytest
from cracking_practices.comparing_str_with_baskspaces.comparing_str_with_baskspaces import backspace_compare


def test_one():
    # str1="xy#z"
    # str2="xzz#"
    expected = True

    actual = backspace_compare('xp#', 'xyz##')

    assert actual == expected, 'Error on test_one.'



def test_two():
    # str1="xy#z"
    # str2="xyz#"
    expected = True

    actual = backspace_compare('xy#z', 'xzz#')

    assert actual == expected, 'Error on test_two.'


def test_three():
    # str1="xp#"
    # str2="xyz##"
    expected = False

    actual = backspace_compare('xy#z', 'xyz#')

    assert actual == expected, 'Error on test_three.'


def test_four():
    # str1="xp#"
    # str2="xyz##"
    expected = True

    actual = backspace_compare('xywrrmp', 'xywrrmu#p')

    assert actual == expected, 'Error on test_four.'
