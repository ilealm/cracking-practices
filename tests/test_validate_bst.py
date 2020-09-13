import pytest
from cracking_practices.validate_bst.validate_bst import validate_bst, BinarySearchTree

def test_valid_empty():
    expected = False

    actual = validate_bst(BinarySearchTree())

    assert actual == expected, 'Error on test_valid_empty.'


def test_valid_3levels(dummy_valid_3levels_tree):
    expected = True

    actual = validate_bst(dummy_valid_3levels_tree)

    assert actual == expected, 'Error on test_valid_3levels.'


def test_unvalid_right_3levels(dummy_valid_3levels_tree):
    expected = False
    dummy_valid_3levels_tree.root.right.right.value = 10

    actual = validate_bst(dummy_valid_3levels_tree)

    assert actual == expected, 'Error on test_unvalid_right_3levels.'


def test_unvalid_left_3levels(dummy_valid_3levels_tree):
    expected = False
    dummy_valid_3levels_tree.root.left.left.right.value = 400

    actual = validate_bst(dummy_valid_3levels_tree)

    assert actual == expected, 'Error on test_unvalid_left_3levels.'



def test_valid_4levels(dummy_valid_4levels_tree):
    expected = True

    actual = validate_bst(dummy_valid_4levels_tree)

    assert actual == expected, 'Error on test_valid_4levels.'

def test_unvalid_left_4levels(dummy_valid_4levels_tree):
    expected = False
    dummy_valid_4levels_tree.root.left.right.left.value = 500

    actual = validate_bst(dummy_valid_4levels_tree)

    assert actual == expected, 'Error on test_unvalid_left_4levels.'

def test_unvalid_left_4levels(dummy_valid_4levels_tree):
    expected = False
    dummy_valid_4levels_tree.root.right.left.value = 50

    actual = validate_bst(dummy_valid_4levels_tree)

    assert actual == expected, 'Error on test_unvalid_left_4levels.'


def test_valid_letters():
    BST = BinarySearchTree()
    # level 0
    BST.add('d')
    # level 1
    BST.add('b')
    BST.add('f')
    # level 2
    BST.add('a')
    BST.add('c')
    BST.add('e')
    BST.add('g')

    expected = True

    actual = validate_bst(BST)

    assert actual == expected, 'Error on test_valid_letters.'


def test_unvalid_left_letters():
    BST = BinarySearchTree()
    # level 0
    BST.add('d')
    # level 1
    BST.add('b')
    BST.add('f')
    # level 2
    BST.add('a')
    BST.add('c')
    BST.add('e')
    BST.add('g')

    expected = False
    BST.root.left.right.value = 'z'

    actual = validate_bst(BST)

    assert actual == expected, 'Error on test_unvalid_left_letters.'


def test_unvalid_right_letters():
    BST = BinarySearchTree()
    # level 0
    BST.add('d')
    # level 1
    BST.add('b')
    BST.add('f')
    # level 2
    BST.add('a')
    BST.add('c')
    BST.add('e')
    BST.add('g')

    expected = False
    BST.root.right.value = 'a'

    actual = validate_bst(BST)

    assert actual == expected, 'Error on test_unvalid_right_letters.'



@pytest.fixture
def dummy_valid_3levels_tree():
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
    # # level 3
    BST.add(15)
    BST.add(40)
    BST.add(60)
    BST.add(90)
    BST.add(115)
    BST.add(140)
    BST.add(160)
    BST.add(190)

    return BST


@pytest.fixture
def dummy_valid_4levels_tree(dummy_valid_3levels_tree):
    # level 4
    dummy_valid_3levels_tree.add(5)
    dummy_valid_3levels_tree.add(20)
    dummy_valid_3levels_tree.add(30)
    dummy_valid_3levels_tree.add(45)
    dummy_valid_3levels_tree.add(55)
    dummy_valid_3levels_tree.add(65)
    dummy_valid_3levels_tree.add(80)
    dummy_valid_3levels_tree.add(95)
    dummy_valid_3levels_tree.add(110)
    dummy_valid_3levels_tree.add(120)
    dummy_valid_3levels_tree.add(130)
    dummy_valid_3levels_tree.add(145)
    dummy_valid_3levels_tree.add(150)
    dummy_valid_3levels_tree.add(165)
    dummy_valid_3levels_tree.add(180)
    dummy_valid_3levels_tree.add(200)
    dummy_valid_3levels_tree.add(40)

    return dummy_valid_3levels_tree
