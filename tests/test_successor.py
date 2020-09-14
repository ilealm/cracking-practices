import pytest
from cracking_practices.successor.successor import successor, BinarySearchTree


def test_node75(dummy_4level_tree):
    # node 75
    node = dummy_4level_tree.root.left.right

    expected = 80

    actual = successor(node)

    assert expected == actual, 'Error on test_node75.'


def test_node150(dummy_4level_tree):
    # node 150
    node = dummy_4level_tree.root.right

    expected = 151

    actual = successor(node)

    assert expected == actual, 'Error on test_node150.'


def test_node110(dummy_4level_tree):
    # node 150
    node = dummy_4level_tree.root.right.left.left.left

    expected = None

    actual = successor(node)

    assert expected == actual, 'Error on test_node110.'


def test_root(dummy_4level_tree):
    # node root (100)
    node = dummy_4level_tree.root

    expected = 110

    actual = successor(node)

    assert expected == actual, 'Error on test_root.'


def test_node15(dummy_4level_tree):
    # node 15
    node = dummy_4level_tree.root.left.left.left

    expected = 20

    actual = successor(node)

    assert expected == actual, 'Error on test_node15.'



@pytest.fixture
def dummy_4level_tree():
    BST = BinarySearchTree()
    # level 0
    BST.add(100)
    # level 1
    BST.add(50)
    BST.add(150)
    # level 2
    BST.add(25)
    BST.add(75)
    BST.add(125)
    BST.add(175)
    # level 3
    BST.add(15)
    BST.add(40)
    BST.add(60)
    BST.add(90)
    BST.add(115)
    BST.add(140)
    BST.add(160)
    BST.add(190)
    # level 4
    BST.add(5)
    BST.add(20)
    BST.add(30)
    BST.add(45)
    BST.add(55)
    BST.add(65)
    BST.add(80)
    BST.add(95)
    BST.add(110)
    BST.add(120)
    BST.add(130)
    BST.add(145)
    BST.add(151)
    BST.add(165)
    BST.add(180)
    BST.add(200)

    return BST


