import pytest
from cracking_practices.linked_list_reverse.linked_list_reverse import Node, LinkedList


def test_reverse_four_nodes():
    ll = LinkedList()
    ll.append_top(40)
    ll.append_top(30)
    ll.append_top(20)
    ll.append_top(10)
    ll.reverse()

    expected = "Head => [40] -> [30] -> [20] -> [10] ->  None"

    actual = ll.traverse()

    assert actual == expected, 'Error on test_reverse_four_nodes.'


def test_reverse_empty():
    ll = LinkedList()
    ll.reverse()

    expected = None

    actual = ll.traverse()

    assert actual == expected, 'Error on test_reverse_empty.'



def test_reverse_two_nodes():
    ll = LinkedList()
    ll.append_top(20)
    ll.append_top(10)
    ll.reverse()

    expected = "Head => [20] -> [10] ->  None"

    actual = ll.traverse()

    assert actual == expected, 'Error on test_reverse_two_nodes.'


def test_reverse_one_nodes():
    ll = LinkedList()
    ll.append_top(10)
    ll.reverse()

    expected = "Head => [10] ->  None"

    actual = ll.traverse()

    assert actual == expected, 'Error on test_reverse_one_nodes.'



def test_reverse_four_nodes():
    ll = LinkedList()
    ll.append_top(100)
    ll.append_top(90)
    ll.append_top(80)
    ll.append_top(70)
    ll.append_top(60)
    ll.append_top(50)
    ll.append_top(40)
    ll.append_top(30)
    ll.append_top(20)
    ll.append_top(10)
    ll.reverse()

    expected = "Head => [100] -> [90] -> [80] -> [70] -> [60] -> [50] -> [40] -> [30] -> [20] -> [10] ->  None"

    actual = ll.traverse()

    assert actual == expected, 'Error on test_reverse_four_nodes.'
