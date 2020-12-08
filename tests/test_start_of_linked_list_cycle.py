import pytest
from cracking_practices.start_of_linked_list_cycle.start_of_linked_list_cycle import Node, find_cycle_start


def test_one(dummy_ll):
    dummy_ll.next.next.next.next.next.next = dummy_ll.next.next

    expected = 3

    actual = find_cycle_start(dummy_ll)

    assert actual == expected, 'Error on test_one.'



def test_two(dummy_ll):
    dummy_ll.next.next.next.next.next.next = dummy_ll.next.next.next

    expected = 4

    actual = find_cycle_start(dummy_ll)

    assert actual == expected, 'Error on test_two.'


def test_three(dummy_ll):
    dummy_ll.next.next.next.next.next.next = dummy_ll

    expected = 1

    actual = find_cycle_start(dummy_ll)

    assert actual == expected, 'Error on test_three.'


@pytest.fixture
def dummy_ll():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  return head





