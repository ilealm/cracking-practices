import pytest
from cracking_practices.tries.tries import Trie


def test_create_emtpy_trie():
    expected = "root"

    actual = Trie().root.value

    assert expected == actual, 'Error on test test_create_emtpy_trie.'


def test_insert():
    trie = Trie()
    trie.insert("cat")

    assert trie.contains("cat"), "Error on test_insert."


def test_contains_one():
    trie = Trie()
    trie.insert("CaNadA")
    assert trie.contains("canada") == True, "Error on test_contains_one."


def test_contains_two():
    trie = Trie()
    trie.insert("CaNadA")
    assert trie.contains("can") == False, "Error on test_contains_two."


def test_contains_tree():
    trie = Trie()
    trie.insert("CaNadA")
    assert trie.contains(None) == False, "Error on test_contains_tree."


def test_contains_four():
    trie = Trie()
    trie.insert("CaNadA")
    assert trie.contains("  caNAda ") == True, "Error on test_contains_four."


def test_contains_five():
    trie = Trie()
    trie.insert("CaNadA")
    assert trie.contains("") == False, "Error on test_contains_five."

