import pytest
from cracking_practices.graphs.graphs import Graph


def test_one(base_graph_with_edge):

    expected = True

    actual = base_graph_with_edge._key_already_exist_in_nodes("Bob")

    assert actual == expected, "Error on test_one."


def test_two(base_graph_with_edge):

    expected = False

    actual = base_graph_with_edge._key_already_exist_in_nodes("Someone")

    assert actual == expected, "Error on test_two."


def test_remove_node(base_graph_with_edge):

    expected = None

    actual = base_graph_with_edge.remove_node("John")

    assert actual == expected, "Error on test_remove_node."


def test_traverse_breathfirst_one():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("D", "C")

    expected = {'A', 'B', 'C', 'D'}
    actual = graph.traverse_breath()

    assert expected == actual, "Error on test_traverse_breathfirst_one."


def test_traverse_breathfirst_two():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")



    expected = {'A'}
    actual = graph.traverse_breath()

    assert expected == actual, "Error on test_traverse_breathfirst_two."


def test_traverse_breathfirst_three():
    graph = Graph()

    expected = None
    actual = graph.traverse_breath()

    assert expected == actual, "Error on test_traverse_breathfirst_three."



@pytest.fixture
def base_graph_with_edge():
    graph = Graph()
    graph.add_node("John")
    graph.add_node("Mary")
    graph.add_node("Bob")
    graph.add_node("Alice")
    graph.add_node("Dan")
    graph.add_node("Nina")

    graph.add_edge("John", "Mary")
    graph.add_edge("John", "Bob")
    graph.add_edge("Bob", "John")
    graph.add_edge("Mary", "John")
    graph.add_edge("Alice", "Mary")
    graph.add_edge("Dan", "Nina")

    return graph


# sdf
