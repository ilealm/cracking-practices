import pytest

from cracking_practices.return_ordered_list.return_ordered_list import return_ordered_list_using_ll, return_ordered_list_using_BST

def test_using_ll_one():
    test = [30, 30, 50, 70, 50, 35, 35, 35, 35, 90, 10, 22, 30, 1, 1, 1, 1, 1, 100]
    expected = [1, 1, 1, 1, 1, 10, 22, 30, 30, 30, 35, 35, 35, 35, 50, 50, 70, 90, 100]

    actual = return_ordered_list_using_ll(test)

    assert actual ==  expected, 'Error on test_using_ll_one'


def test_using_ll_two():
    test = [90,80,70,60,50,50,50,20,90,100]
    expected = [20,50,50,50,60,70,80,90,90,100]

    actual = return_ordered_list_using_ll(test)

    assert actual ==  expected, 'Error on test_using_ll_two'


def test_using_ll_three():
    test = [90]
    expected = [90]

    actual = return_ordered_list_using_ll(test)

    assert actual ==  expected, 'Error on test_using_ll_three'


def test_using_ll_four():
    test = []
    expected = []

    actual = return_ordered_list_using_ll(test)

    assert actual ==  expected, 'Error on test_using_ll_four'


def test_using_ll_five():
    test = [10,15,20,25,25,25,20,15,10,75,60]
    expected = [10,10,15,15,20,20,25,25,25,60,75]

    actual = return_ordered_list_using_ll(test)

    assert actual ==  expected, 'Error on test_using_ll_five'



# TEST ON TREE

def test_using_BST_one():
    test = [30, 30, 50, 70, 50, 35, 35, 35, 35, 90, 10, 22, 30, 1, 1, 1, 1, 1, 100]
    expected = [1, 1, 1, 1, 1, 10, 22, 30, 30, 30, 35, 35, 35, 35, 50, 50, 70, 90, 100]

    actual = return_ordered_list_using_BST(test)

    assert actual ==  expected, 'Error on test_using_BST_one'


def test_using_BST_two():
    test = [90,80,70,60,50,50,50,20,90,100]
    expected = [20,50,50,50,60,70,80,90,90,100]

    actual = return_ordered_list_using_BST(test)

    assert actual ==  expected, 'Error on test_using_BST_two'


def test_using_BST_three():
    test = [90]
    expected = [90]

    actual = return_ordered_list_using_BST(test)

    assert actual ==  expected, 'Error on test_using_BST_three'


def test_using_BST_four():
    test = []
    expected = []

    actual = return_ordered_list_using_BST(test)

    assert actual ==  expected, 'Error on test_using_BST_four'


def test_using_BST_five():
    test = [10,15,20,25,25,25,20,15,10,75,60]
    expected = [10,10,15,15,20,20,25,25,25,60,75]

    actual = return_ordered_list_using_BST(test)

    assert actual ==  expected, 'Error on test_using_BST_five'
