import pytest
from cracking_practices.middle_of_linkedlist.middle_of_linkedlist import Node, find_middle_of_linked_list

def test_one(dummy_ll):

    expected = 3

    actual = find_middle_of_linked_list(dummy_ll)

    assert actual == expected, 'Error on test_one.'



def test_two(dummy_ll):
    dummy_ll.next.next.next.next.next = Node(6)
    dummy_ll.next.next.next.next.next.next = Node(7)

    expected = 4

    actual = find_middle_of_linked_list(dummy_ll)

    assert actual == expected, 'Error on test_two.'


def test_three(dummy_ll):
    dummy_ll.next.next.next.next.next = Node(6)

    expected = 4

    actual = find_middle_of_linked_list(dummy_ll)

    assert actual == expected, 'Error on test_three.'


@pytest.fixture
def dummy_ll():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  return head

