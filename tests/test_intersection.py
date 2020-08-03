import pytest
from cracking_practices.intersection.intersection import Node, LinkedList, interseccion_approach_one


def test_interseccion_approach_one_true():
    one = LinkedList()
    one.insert('E')
    one.insert('D')
    node_c = one.insert('C')
    one.insert('B')
    one.insert('A')
    two = LinkedList()
    two.insert('Z',node_c)
    two.insert('Y')
    two.insert('X')

    expected = node_c

    actual = interseccion_approach_one(one, two)
    assert actual == expected, "Error on test_interseccion_approach_one_true."


def test_interseccion_approach_one_false():
    one = LinkedList()
    one.insert('E')
    one.insert('D')
    one.insert('C')
    one.insert('B')
    one.insert('A')
    two = LinkedList()
    two.insert('Z')
    two.insert('Y')
    two.insert('X')

    expected = False

    actual = interseccion_approach_one(one, two)
    assert actual == expected, "Error on test_interseccion_approach_one_false."


def test_interseccion_approach_one_words():
    one = LinkedList()
    apple= one.insert('apple')
    one.insert('strawberry')
    one.insert('pinapple')
    one.insert('grapes')
    one.insert('oranges')

    two = LinkedList()
    two.insert('bread', apple)
    two.insert('cookies')
    two.insert('ice cream')
    one.insert('watermelon')

    expected = apple

    actual = interseccion_approach_one(one, two)
    assert actual == expected, "Error on test_interseccion_approach_one_words."


def test_interseccion_approach_one_node():
    one = LinkedList()
    apple= one.insert('apple')

    two = LinkedList()
    two.insert('bread', apple)
    expected = apple

    actual = interseccion_approach_one(one, two)
    assert actual == expected, "Error on test_interseccion_approach_one_node."


def test_interseccion_approach_one_empty():
    one = LinkedList()
    one.insert('apple')
    one.insert('strawberry')
    one.insert('pinapple')
    one.insert('grapes')
    one.insert('oranges')

    two = LinkedList()

    expected = False
    actual = interseccion_approach_one(one, two)

    assert actual == expected, "Error on test_interseccion_approach_one_node."
