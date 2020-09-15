import pytest
from cracking_practices.get_node_path.get_node_path import get_node_path, BinarySearchTree


def test_get_node_path_none(dummy_4level_BST):
    node = None

    expected = []

    actual =get_node_path(dummy_4level_BST, node)

    assert actual == expected, 'Error on test_get_node_path_none.'


def test_get_node_path20(dummy_4level_BST):
    # Node: 20
    node = dummy_4level_BST.root.left.left.left.right

    expected = [15, 25, 50, 100]

    actual =get_node_path(dummy_4level_BST, node)

    assert actual == expected, 'Error on test_get_node_path20.'


def test_get_node_path90(dummy_4level_BST):
    # Node: 90
    node = dummy_4level_BST.root.left.right.right

    expected = [75, 50, 100]

    actual =get_node_path(dummy_4level_BST, node)

    assert actual == expected, 'Error on test_get_node_path90.'


def test_get_node_path145(dummy_4level_BST):
    # Node: 145
    node = dummy_4level_BST.root.right.left.right.right

    expected = [140, 125, 150, 100]

    actual =get_node_path(dummy_4level_BST, node)

    assert actual == expected, 'Error on test_get_node_path145.'


def test_get_node_path200(dummy_4level_BST):
    # Node: 200
    node = dummy_4level_BST.root.right.right.right.right

    expected = [190, 175, 150, 100]

    actual =get_node_path(dummy_4level_BST, node)

    assert actual == expected, 'Error on test_get_node_path200.'


def test_get_node_path_root(dummy_4level_BST):
    # Node: 100
    node = dummy_4level_BST.root

    expected = [100]

    actual =get_node_path(dummy_4level_BST, node)

    assert actual == expected, 'Error on test_get_node_path_root.'




@pytest.fixture
def dummy_4level_BST():
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
