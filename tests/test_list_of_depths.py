import pytest
from cracking_practices.list_of_depths.list_of_depths import list_of_depths, BinarySearchTree

def test_list_of_depths_zero():
    BST = BinarySearchTree()

    expected = []

    actual = list_of_depths(BST)

    assert actual == expected, 'Error on test_list_of_depths_zero.'


def test_list_of_depths_one():
    BST = BinarySearchTree()
    # level 0
    BST.add(100)
    # level 1
    BST.add(50)
    BST.add(150)

    expected = ['The head is 100 -> None', 'The head is 50 -> 150 -> None']

    actual = list_of_depths(BST)

    assert actual == expected, 'Error on test_list_of_depths_one.'



def test_list_of_depths_two():
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

    expected = ['The head is 100 -> None', 'The head is 50 -> 150 -> None', 'The head is 25 -> 75 -> 125 -> 175 -> None', 'The head is 15 -> 40 -> 60 -> 90 -> 115 -> 140 -> 160 -> 190 -> None']

    actual = list_of_depths(BST)

    assert actual == expected, 'Error on test_list_of_depths_two.'


def test_list_of_depths_three():
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

    expected = ['The head is 100 -> None', 'The head is 50 -> 150 -> None', 'The head is 25 -> 75 -> 125 -> 175 -> None', 'The head is 15 -> 40 -> 60 -> 90 -> 115 -> 140 -> 160 -> 190 -> None', 'The head is 5 -> 20 -> 30 -> 45 -> 55 -> 65 -> 80 -> 95 -> 110 -> 120 -> 130 -> 145 -> 150 -> 165 -> 180 -> 200 -> None']

    actual = list_of_depths(BST)

    assert actual == expected, 'Error on test_list_of_depths_three.'



def test_list_of_depths_four():
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
    BST.add(90)
    BST.add(115)
    BST.add(160)
    BST.add(190)
    # level 4
    BST.add(5)
    BST.add(20)
    BST.add(45)
    BST.add(80)
    BST.add(95)
    BST.add(110)
    BST.add(150)
    BST.add(165)
    BST.add(180)

    expected = ['The head is 100 -> None', 'The head is 50 -> 150 -> None', 'The head is 25 -> 75 -> 125 -> 175 -> None', 'The head is 15 -> 40 -> 90 -> 115 -> 160 -> 190 -> None', 'The head is 5 -> 20 -> 45 -> 80 -> 95 -> 110 -> 150 -> 165 -> 180 -> None']

    actual = list_of_depths(BST)

    assert actual == expected, 'Error on test_list_of_depths_four.'
