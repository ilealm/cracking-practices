import pytest
from cracking_practices.loop_detection.loop_detection import Node, LinkedList, loop_detection

def test_one():
    circular = LinkedList()
    circular.insert('D')
    node_c = circular.insert('C')
    circular.insert('B')
    circular.insert('A')
    circular.append('E', node_c)

    expected = node_c

    actual = circular.head.next.next.next.next.next
    assert actual == expected, "Error on test_one."


def test_two():
    circular = LinkedList()
    circular.insert('D')
    node_c = circular.insert('C')
    circular.insert('B')
    circular.insert('A')
    circular.append('E', node_c)

    expected = node_c

    actual = loop_detection(circular)
    assert actual == expected, "Error on test_two."


def test_three():
    circular = LinkedList()
    circular.insert('D')
    circular.insert('C')
    circular.insert('B')
    circular.insert('A')
    circular.append('E')

    expected = False

    actual = loop_detection(circular)
    assert actual == expected, "Error on test_three."


def test_four():
    circular = LinkedList()

    expected = False

    actual = loop_detection(circular)
    assert actual == expected, "Error on test_four."


def test_five():
    circular = LinkedList()
    circular.insert('D')
    circular.insert('C')
    circular.insert('B')
    node_a = circular.insert('A')
    circular.append('E', node_a)

    expected = node_a

    actual = loop_detection(circular)
    assert actual == expected, "Error on test_five."
