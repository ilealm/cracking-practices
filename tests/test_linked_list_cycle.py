import pytest
from cracking_practices.linked_list_cycle.linked_list_cycle import Node, has_cycle


def test_one(dummy_linked_list):

    expected = False

    actual = has_cycle(dummy_linked_list)

    assert actual == expected, 'Error on test_one.'



def test_two(dummy_linked_list):

    dummy_linked_list.next.next.next.next.next.next = dummy_linked_list.next.next

    expected = True

    actual = has_cycle(dummy_linked_list)

    assert actual == expected, 'Error on test_two.'


def test_three(dummy_linked_list):

    dummy_linked_list.next.next.next.next.next.next = dummy_linked_list.next.next.next

    expected = True

    actual = has_cycle(dummy_linked_list)

    assert actual == expected, 'Error on test_three.'



@pytest.fixture
def dummy_linked_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    return head

