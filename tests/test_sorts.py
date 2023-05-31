import pytest
from cracking_practices.sorts.sorts import BubbleSort, SelectionSort, InsertionSort


def test_bubble_sort_one():
    sort = BubbleSort([8, 2, 4, 1, 3, 6, 0])

    expected = [0, 1, 2, 3, 4, 6, 8]

    actual = sort.sort()

    assert actual == expected, "Error on test_bubble_sort_one"


def test_bubble_sort_two():
    sort = BubbleSort([9, 1, 50, 1, 7])

    expected = [1, 1, 7, 9, 50]

    actual = sort.sort()

    assert actual == expected, "Error on test_bubble_sort_two"


def test_bubble_sort_three():
    sort = BubbleSort([])

    expected = []

    actual = sort.sort()

    assert actual == expected, "Error on test_bubble_sort_three"


def test_bubble_sort_four():
    sort = BubbleSort([7, 3])

    expected = [3, 7]

    actual = sort.sort()

    assert actual == expected, "Error on test_bubble_sort_four"


def test_bubble_sort_five():
    sort = BubbleSort([7])

    expected = [7]

    actual = sort.sort()

    assert actual == expected, "Error on test_bubble_sort_five"


def test_selecction_sort_one():
    sort = SelectionSort([7])

    expected = [7]

    actual = sort.sort()

    assert actual == expected, "Error on test_selecction_sort_one"


def test_selecction_sort_two():
    sort = SelectionSort([9, 1, 5, 10, 7])

    expected = [1, 5, 7, 9, 10]

    actual = sort.sort()

    assert actual == expected, "Error on test_selecction_sort_two"


def test_selecction_sort_three():
    sort = SelectionSort([9, 1])

    expected = [1, 9]

    actual = sort.sort()

    assert actual == expected, "Error on test_selecction_sort_three"


def test_selecction_sort_four():
    sort = SelectionSort([])

    expected = []

    actual = sort.sort()

    assert actual == expected, "Error on test_selecction_sort_four"


def test_selecction_sort_five():
    sort = SelectionSort([100])

    expected = [100]

    actual = sort.sort()

    assert actual == expected, "Error on test_selecction_sort_five"



def test_insertion_sort_one():
    sort = InsertionSort([8,2,4,1,3])

    expected = [1,2,3,4,8]

    actual = sort.sort()

    assert actual == expected, "Error on test_insertion_sort_one"


def test_insertion_sort_two():
    sort = InsertionSort([8])

    expected = [8]

    actual = sort.sort()

    assert actual == expected, "Error on test_insertion_sort_two"


def test_insertion_sort_three():
    sort = InsertionSort([8, 1])

    expected = [1, 8]

    actual = sort.sort()

    assert actual == expected, "Error on test_insertion_sort_three"


def test_insertion_sort_three():
    sort = InsertionSort([ 0, 8, 1])

    expected = [0, 1, 8]

    actual = sort.sort()

    assert actual == expected, "Error on test_insertion_sort_three"


def test_insertion_sort_three():
    sort = InsertionSort([])

    expected = []

    actual = sort.sort()

    assert actual == expected, "Error on test_insertion_sort_three"
