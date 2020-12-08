import pytest
from cracking_practices.linked_list_cycle_length.linked_list_cycle_length import Node, find_cycle_length


def test_one():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    expected = 0

    actual = find_cycle_length(head)

    assert actual == expected, 'Error on test_one.'


def test_two():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next.next

    expected = 3

    actual = find_cycle_length(head)

    assert actual == expected, 'Error on test_two.'


def test_three():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next

    expected = 4

    actual = find_cycle_length(head)

    assert actual == expected, 'Error on test_three.'
