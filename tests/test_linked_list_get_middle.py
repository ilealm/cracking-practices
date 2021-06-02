import pytest
from cracking_practices.linked_list_get_middle.linked_list_get_middle import Node, LinkedList


def test_ten_nodes(dummy_ten_nodes):
    expected = 50

    actual = dummy_ten_nodes.get_middle_node()

    assert actual == expected, 'Error on test_ten_nodes.'


def test_eleven_nodes(dummy_ten_nodes):
    dummy_ten_nodes.add(0)
    expected = 50

    actual = dummy_ten_nodes.get_middle_node()

    assert actual == expected, 'Error on test_eleven_nodes.'


def test_empty():
    ll = LinkedList()
    expected = "The list is empty."

    actual = ll.get_middle_node()

    assert actual == expected, 'Error on test_empty.'


def test_two_nodes():
    ll = LinkedList()
    ll.add(20)
    ll.add(10)
    expected = 10

    actual = ll.get_middle_node()

    assert actual == expected, 'Error on test_two_nodes.'


def test_three_nodes():
    ll = LinkedList()
    ll.add(30)
    ll.add(20)
    ll.add(10)
    expected = 20

    actual = ll.get_middle_node()

    assert actual == expected, 'Error on test_three_nodes.'



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
