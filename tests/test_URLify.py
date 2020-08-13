import pytest
from cracking_practices.URLify.URLify import URLify


def test_URLify_one():
    str_to_url = 'Mr. John Smith    '
    letters_count = 13

    expected = 'Mr.%20John%20Smith'

    actual = URLify(str_to_url,letters_count)

    assert actual == expected, "Error on tes_URLify_one."



def test_URLify_two():
    str_to_url = 'car'
    letters_count = 3

    expected = 'car'

    actual = URLify(str_to_url,letters_count)

    assert actual == expected, "Error on test_URLify_two."

def test_URLify_three():
    str_to_url = ''
    letters_count = 0

    expected = ''

    actual = URLify(str_to_url,letters_count)

    assert actual == expected, "Error on test_URLify_three."


def test_URLify_four():
    str_to_url = '   craking practices   '
    letters_count = 20

    expected = 'craking%20practices'

    actual = URLify(str_to_url,letters_count)

    assert actual == expected, "Error on test_URLify_four."
