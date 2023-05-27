import pytest
from cracking_practices.weighted_graphs.weighted_graphs import Path, NodeEntry, Node, Edge, WightedGraph

def test_one():
    g  = WightedGraph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")

    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 2)
    g.add_edge("A", "C", 10)
    expected = 'A B C'
    # expected = ['A', 'B', 'C']

    actual = g.get_shortest_path("A", "C")

    assert actual == expected, 'Error on test_one.'
