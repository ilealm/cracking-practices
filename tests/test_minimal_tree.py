import pytest
from cracking_practices.minimal_tree.minimal_tree import minimal_tree

def test_minimal_tree_one():
    array = [15, 25, 40, 50, 60, 75, 90, 100, 115, 125, 140, 150, 160, 175, 190]

    expected = [100, 50, 150, 25, 75, 125, 175, 15, 40, 60, 90, 115, 140, 160, 190]

    actual = minimal_tree(array).BreadthFirst()

    assert actual == expected, 'Error on test_minimal_tree_one.'



def test_minimal_tree_two():
    array = [5, 15, 20,25, 30,40,45,50,55,60,65]

    expected = [40, 20, 55, 15, 30, 50, 65, 5, 25, 45, 60]

    actual = minimal_tree(array).BreadthFirst()

    assert actual == expected, 'Error on test_minimal_tree_two.'


def test_minimal_tree_tree():
    array = [5, 15, 20,25, 30,40,45, 50,55, 60,65, 75, 80,90, 95, 100, 110, 115, 120, 130, 125, 140, 145, 150, 160, 165, 180, 175, 190, 200]

    expected = [100, 50, 150, 25, 75, 130, 175, 15, 40, 60, 90, 115, 140, 165, 180, 5, 20, 30, 45, 55, 65, 80, 95, 110, 120, 145, 160, 200, 125, 190]

    actual = minimal_tree(array).BreadthFirst()

    assert actual == expected, 'Error on test_minimal_tree_tree.'
