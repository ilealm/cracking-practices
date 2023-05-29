import pytest
from cracking_practices.sorts.sorts import BubbleSort

def test_bubble_sort_one():
    sort = BubbleSort([8, 2, 4, 1, 3, 6, 0])

    expected = [0, 1, 2, 3, 4, 6, 8]

    actual = sort.sort()

    assert actual == expected,  'Error on test_bubble_sort_one'


def test_bubble_sort_two():
    sort = BubbleSort([9 , 1, 50, 1,  7])

    expected = [1,1,7,9,50]

    actual = sort.sort()

    assert actual == expected,  'Error on test_bubble_sort_two'



def test_bubble_sort_three():
    sort = BubbleSort([])

    expected = []

    actual = sort.sort()

    assert actual == expected,  'Error on test_bubble_sort_three'
