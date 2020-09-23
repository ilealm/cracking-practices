import pytest
from cracking_practices.bst_sequences.bst_sequences import bst_sequences, BinarySearchTree

def test_one():
    BST = BinarySearchTree()
    BST.add(2)
    BST.add(1)
    BST.add(3)

    expected = [[2, 1, 3], [2, 3, 1]]

    actual = bst_sequences(BST)

    assert actual == expected, 'Error on test_one.'

def test_two():
    BST = BinarySearchTree()
    BST.add(2)
    BST.add(1)
    BST.add(3)
    BST.add(4)

    expected = [[2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1]]

    actual = bst_sequences(BST)

    assert actual == expected, 'Error on test_two.'
