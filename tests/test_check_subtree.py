import pytest
from cracking_practices.check_subtree.check_subtree import BinarySearchTree, check_subtree

def test_one(dummy_4level, dummy_sub_4level):
    expected = True

    actual = check_subtree(dummy_4level, dummy_sub_4level)

    assert actual == expected, 'Error on test_one.'


def test_two(dummy_4level, dummy_sub_4level):
    dummy_4level.add(97)
    dummy_4level.add(76)
    expected = True

    actual = check_subtree(dummy_4level, dummy_sub_4level)

    assert actual == expected, 'Error on test_two.'


def test_three(dummy_4level):
    BST2 = BinarySearchTree()
    BST2.add(140)
    BST2.add(100)
    BST2.add(200)
    BST2.add(50)
    BST2.add(50)
    BST2.add(150)

    expected = False

    actual = check_subtree(dummy_4level, BST2)

    assert actual == expected, 'Error on test_three.'


def test_four(dummy_4level):
    BST2 = BinarySearchTree()
    BST2.add(75)
    BST2.add(60)
    BST2.add(90)
    BST2.add(55)

    expected = True

    actual = check_subtree(dummy_4level, BST2)

    assert actual == expected, 'Error on test_four.'


def test_five(dummy_4level):
    BST2 = BinarySearchTree()
    BST2.add(75)
    BST2.add(60)
    BST2.add(90)
    BST2.add(56)

    expected = False

    actual = check_subtree(dummy_4level, BST2)

    assert actual == expected, 'Error on test_five.'


def test_five(dummy_4level):
    expected = False

    actual = check_subtree(dummy_4level, None)

    assert actual == expected, 'Error on test_five.'


@pytest.fixture
def dummy_4level():
    BST1 = BinarySearchTree()
    # level 0
    BST1.add(100)
    # level 1
    BST1.add(50)
    BST1.add(150)
    # level 2
    BST1.add(25)
    BST1.add(75)
    BST1.add(125)
    BST1.add(175)
    # level 3
    BST1.add(15)
    BST1.add(40)
    BST1.add(60)
    BST1.add(90)
    BST1.add(115)
    BST1.add(140)
    BST1.add(160)
    BST1.add(190)
    # level 4
    BST1.add(5)
    BST1.add(20)
    BST1.add(30)
    BST1.add(45)
    BST1.add(55)
    BST1.add(65)
    BST1.add(80)
    BST1.add(95)
    BST1.add(110)
    BST1.add(120)
    BST1.add(130)
    BST1.add(145)
    BST1.add(151)
    BST1.add(165)
    BST1.add(180)
    BST1.add(200)

    return BST1


@pytest.fixture
def dummy_sub_4level():
    BST2 = BinarySearchTree()
    BST2.add(175)
    BST2.add(160)
    BST2.add(190)
    BST2.add(151)
    BST2.add(165)
    BST2.add(180)
    BST2.add(200)

    return BST2

