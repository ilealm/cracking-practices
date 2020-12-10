import pytest
from cracking_practices.rearrange_linkedlist.rearrange_linkedlist import Node, reorder


def test_one():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)

    expected = '2 12 4 10 6 8 '

    reorder(head)
    actual = head.print_list()

    assert actual == expected, 'Error on test_one.'



def test_two():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    expected = '1 8 2 7 3 6 4 5 '

    reorder(head)
    actual = head.print_list()

    assert actual == expected, 'Error on test_two.'
