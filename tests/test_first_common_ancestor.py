import pytest
from cracking_practices.first_common_ancestor.first_common_ancestor import get_node_path, BinarySearchTree, first_common_ancestor


def test_node20_node90(dummy_4level_BST):
    # Node: 20
    node_a = dummy_4level_BST.root.left.left.left.right
    # Node: 90
    node_b = dummy_4level_BST.root.left.right.right

    expected = 50

    actual = first_common_ancestor(dummy_4level_BST, node_a, node_b)

    assert actual == expected, 'Error on test_node20_node90.'


def test_node50_node150(dummy_4level_BST):
    # Node: 145
    node_a = dummy_4level_BST.root.left.right.right
    # Node: 200
    node_b = dummy_4level_BST.root.right.right.right.right

    expected = 100

    actual = first_common_ancestor(dummy_4level_BST, node_a, node_b)

    assert actual == expected, 'Error on test_node50_node150.'


def test_node145_node200(dummy_4level_BST):
    # Node: 145
    node_a = dummy_4level_BST.root.left
    # Node: 200
    node_b = dummy_4level_BST.root.right

    expected = 100

    actual = first_common_ancestor(dummy_4level_BST, node_a, node_b)

    assert actual == expected, 'Error on test_node145_node200.'



def test_node120_node130(dummy_4level_BST):
    # Node: 120
    node_a = dummy_4level_BST.root.right.left.left.right
    # Node: 140
    node_b = dummy_4level_BST.root.right.left.right

    expected = 125

    actual = first_common_ancestor(dummy_4level_BST, node_a, node_b)

    assert actual == expected, 'Error on test_node120_node130.'


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
