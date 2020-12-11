import pytest
from cracking_practices.palindrome_singly_ll.palindrome_singly_ll import Node, is_palindromic_linked_list


def test_one(dummy_ll):

    expected = True

    actual = is_palindromic_linked_list(dummy_ll)

    assert actual == expected, 'Error on test_one.'



def test_two(dummy_ll):
    dummy_ll.next.next.next.next.next = Node(2)
    
    expected = False

    actual = is_palindromic_linked_list(dummy_ll)

    assert actual == expected, 'Error on test_two.'





@pytest.fixture
def dummy_ll():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    return head
