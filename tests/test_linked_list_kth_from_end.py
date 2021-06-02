import re
import pytest
from cracking_practices.linked_list_kth_from_end.linked_list_kth_from_end import (
    Node,
    LinkedList,
)


def test_empty():
    ll = LinkedList()
    k = 3
    expected = "The linked list is empty."

    actual = ll.kth_from_end(k)

    assert actual == expected, "Error on test_empty."


def test_bigger_kth(dummy_ten_nodes):
    k = 11
    expected = "Kth value is bigger than the linked list."

    actual = dummy_ten_nodes.kth_from_end(k)

    assert actual == expected, "Error on test_bigger_kth."


def test_3rd(dummy_ten_nodes):
    k = 3
    expected = 70

    actual = dummy_ten_nodes.kth_from_end(k)

    assert actual == expected, "Error on test_3rd."


def test_1rd(dummy_ten_nodes):
    k = 1
    expected = 90

    actual = dummy_ten_nodes.kth_from_end(k)

    assert actual == expected, "Error on test_1rd."


def test_zero(dummy_ten_nodes):
    k = 0
    expected = 100

    actual = dummy_ten_nodes.kth_from_end(k)

    assert actual == expected, "Error on test_zero."



@pytest.fixture
def dummy_ten_nodes():
    ll = LinkedList()
    ll.add(100)
    ll.add(90)
    ll.add(80)
    ll.add(70)
    ll.add(60)
    ll.add(50)
    ll.add(40)
    ll.add(30)
    ll.add(20)
    ll.add(10)

    return ll
