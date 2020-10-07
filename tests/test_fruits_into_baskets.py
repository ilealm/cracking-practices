import pytest
from cracking_practices.fruits_into_baskets.fruits_into_baskets import fruits_into_baskets

def test_one():
    fruits = ['A', 'B', 'C', 'A', 'C']
    expected = 3

    actual = fruits_into_baskets(fruits)

    assert actual ==  expected, 'Error on test_one.'


def test_two():
    fruits = ['A', 'B', 'C', 'B', 'B', 'C']
    expected = 5

    actual = fruits_into_baskets(fruits)

    assert actual ==  expected, 'Error on test_two.'
