import pytest

from cracking_practices.zig_zag_tree.zig_zag_tree import zig_zag_tree, Node, BinaryTree, BinarySearchTree


def test_empty_tree():
    '''
    Test on an empty tree.
    '''

    expected = []

    actual = zig_zag_tree(BinarySearchTree())

    assert actual ==  expected, 'Error on test_empty_tree'


def test_one_node():
    '''
    Test on a tree with only the root
    '''
    BST = BinarySearchTree()
    # level 0
    BST.add(100)

    expected = [100]

    actual = zig_zag_tree(BST)

    assert actual ==  expected, 'Error on test_one_node'


def test_two_nodes():
    '''
    Test on a tree with only two nodes
    '''
    BST = BinarySearchTree()
    # level 0
    BST.add(100)
    BST.add(50)

    expected = [100,50]

    actual = zig_zag_tree(BST)

    assert actual ==  expected, 'Error on nodes.'



def test_32_nodes(dummy_tree_32):
    '''
    Test on a perfectly balanced 4 level binary tree
    '''
    expected = [100, 150, 50, 25, 75, 125, 175, 190, 160, 140, 115, 90, 60, 40, 15, 5, 20, 30, 45, 55, 65, 80, 95, 110, 120, 130, 145, 150, 165, 180, 200]

    actual = zig_zag_tree(dummy_tree_32)

    assert actual ==  expected, 'Error on test_32_nodes'


def test_unbalanced_nodes(dummy_unbalanced_tree):
    '''
    Test on unbalanced 4 level binary tree
    '''
    expected = [100, 150, 50, 25, 75, 125, 175, 190, 160, 140, 115, 90, 60, 40, 15, 5, 20, 45, 55, 80, 95, 120, 130, 150, 165, 180]

    actual = zig_zag_tree(dummy_unbalanced_tree)

    assert actual ==  expected, 'Error on dummy_unbalanced_tree'


def test_2_level_unbalanced(dummy_2_level_unbalanced):
    '''
    Test on unbalanced 2 level binary tree
    '''
    expected = [100, 150, 50, 25, 125]

    actual = zig_zag_tree(dummy_2_level_unbalanced)

    assert actual ==  expected, 'Error on dummy_2_level_unbalanced'




@pytest.fixture
def dummy_tree_32():
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
    BST.add(150)
    BST.add(165)
    BST.add(180)
    BST.add(200)

    return BST


@pytest.fixture
def dummy_unbalanced_tree():
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



@pytest.fixture
def dummy_2_level_unbalanced():
    BST = BinarySearchTree()
    # level 0
    BST.add(100)
    # level 1
    BST.add(50)
    BST.add(150)
    # level 2
    BST.add(25)
    BST.add(125)

    return BST
