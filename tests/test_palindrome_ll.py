import pytest
from cracking_practices.palindrome_ll.palindrome_ll import LinkedList, Node, DoublyLinkedList, DoublyNode, palindrome_singly_ll, palindrome_doubly_ll

def test_palindrome_singly_ll_kayak():
    singly_ll = LinkedList()
    singly_ll.insert('k')
    singly_ll.insert('a')
    singly_ll.insert('y')
    singly_ll.insert('a')
    singly_ll.insert('k')
    expected = True

    actual = palindrome_singly_ll(singly_ll)

    assert actual == expected, "Error on test_palindrome_singly_ll_kayak."


def test_palindrome_singly_ll_Mom():
    singly_ll = LinkedList()
    singly_ll.insert('M')
    singly_ll.insert('o')
    singly_ll.insert('m')
    expected = True

    actual = palindrome_singly_ll(singly_ll)

    assert actual == expected, "Error on test_palindrome_singly_ll_Mom."


def test_palindrome_singly_ll_abcde():
    singly_ll = LinkedList()
    singly_ll.insert('a')
    singly_ll.insert('b')
    singly_ll.insert('c')
    singly_ll.insert('d')
    singly_ll.insert('e')
    expected = False

    actual = palindrome_singly_ll(singly_ll)

    assert actual == expected, "Error on test_palindrome_singly_ll_abcde."


def test_palindrome_singly_ll_word():
    singly_ll = LinkedList()
    singly_ll.insert('w')
    singly_ll.insert('o')
    singly_ll.insert('r')
    singly_ll.insert('d')
    expected = False

    actual = palindrome_singly_ll(singly_ll)

    assert actual == expected, "Error on test_palindrome_singly_ll_word."

def test_palindrome_singly_ll_noon():
    singly_ll = LinkedList()
    singly_ll.insert('n')
    singly_ll.insert('o')
    singly_ll.insert('o')
    singly_ll.insert('n')
    expected = True

    actual = palindrome_singly_ll(singly_ll)

    assert actual == expected, "Error on test_palindrome_singly_ll_noon."


def test_palindrome_singly_ll_empty():
    singly_ll = LinkedList()
    expected = False

    actual = palindrome_singly_ll(singly_ll)

    assert actual == expected, "Error on test_palindrome_singly_ll_empty."


def test_palindrome_singly_ll_one_word():
    singly_ll = LinkedList()
    singly_ll.insert('a')
    expected = True

    actual = palindrome_singly_ll(singly_ll)

    assert actual == expected, "Error on test_palindrome_singly_ll_single."


def palindrome_doubly_ll_kayak():
    doubly_ll = DoublyLinkedList()
    doubly_ll.insert('k')
    doubly_ll.insert('a')
    doubly_ll.insert('y')
    doubly_ll.insert('a')
    doubly_ll.insert('k')
    expected = True

    actual = palindrome_doubly_ll(doubly_ll)

    assert actual == expected, "Error on palindrome_doubly_ll_kayak."



def palindrome_doubly_ll_Mon():
    doubly_ll = DoublyLinkedList()
    doubly_ll.insert('M')
    doubly_ll.insert('o')
    doubly_ll.insert('m')
    expected = True

    actual = palindrome_doubly_ll(doubly_ll)

    assert actual == expected, "Error on palindrome_doubly_ll_Mom."



def palindrome_doubly_ll_abcde():
    doubly_ll = DoublyLinkedList()
    doubly_ll.insert('a')
    doubly_ll.insert('b')
    doubly_ll.insert('c')
    doubly_ll.insert('d')
    doubly_ll.insert('e')
    expected = False

    actual = palindrome_doubly_ll(doubly_ll)

    assert actual == expected, "Error on palindrome_doubly_ll_abcde."


def palindrome_doubly_ll_word():
    doubly_ll = DoublyLinkedList()
    doubly_ll.insert('w')
    doubly_ll.insert('o')
    doubly_ll.insert('r')
    doubly_ll.insert('d')
    expected = False

    actual = palindrome_doubly_ll(doubly_ll)

    assert actual == expected, "Error on palindrome_doubly_ll_word."


def palindrome_doubly_ll_noon():
    doubly_ll = DoublyLinkedList()
    doubly_ll.insert('n')
    doubly_ll.insert('o')
    doubly_ll.insert('o')
    doubly_ll.insert('n')
    expected = True

    actual = palindrome_doubly_ll(doubly_ll)

    assert actual == expected, "Error on palindrome_doubly_ll_noon."
