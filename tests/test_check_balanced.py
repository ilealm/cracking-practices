import pytest
from cracking_practices.check_balanced.check_balanced import check_balanced, BinarySearchTree

def test_one(dummy_balanced_4levels_tree):
    expected = True

    actual = check_balanced(dummy_balanced_4levels_tree)

    assert actual == expected, 'Error on test_one.'


def test_two(dummy_balanced_4levels_tree):
    expected = True
    dummy_balanced_4levels_tree.add(4)

    actual = check_balanced(dummy_balanced_4levels_tree)

    assert actual == expected, 'Error on test_two.'


def test_tree(dummy_balanced_4levels_tree):
    expected = False
    dummy_balanced_4levels_tree.add(4)
    dummy_balanced_4levels_tree.add(3)

    actual = check_balanced(dummy_balanced_4levels_tree)

    assert actual == expected, 'Error on test_tree.'


def test_four():
    BST = BinarySearchTree()
    # level 0
    BST.add(100)
    # level 1
    BST.add(50)
    # level 2
    BST.add(25)

    BST.add(15)
    BST.add(40)

    expected = False

    actual = check_balanced(BST)

    assert actual == expected, 'Error on test_four.'


def test_five():
    BST = BinarySearchTree()
    # level 0
    BST.add(100)
    BST.add(150)
    # level 1
    BST.add(50)
    # level 2
    BST.add(25)

    BST.add(15)
    BST.add(40)

    expected = False

    actual = check_balanced(BST)

    assert actual == expected, 'Error on test_five.'


@pytest.fixture
def dummy_balanced_4levels_tree():
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
    BST.add(45)
    BST.add(55)
    BST.add(80)
    BST.add(95)
    BST.add(120)
    BST.add(130)
    BST.add(150)
    BST.add(165)
    BST.add(180)

    return BST
