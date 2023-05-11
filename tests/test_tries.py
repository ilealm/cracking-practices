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



def test_delete_existing_word():
    trie = Trie()
    trie.insert("care")
    trie.insert("tree")
    trie.insert("desk")
    word = 'care'
    trie.delete(word)

    assert trie.contains(word) == False, "Error on test_delete_existing_word"


def test_delete_existing_word_with_more_letters_left():
    trie = Trie()
    trie.insert("care")
    trie.insert("tree")
    trie.insert("desk")
    trie.insert("car")
    word = 'car'
    trie.delete(word)

    assert (trie.contains(word) == False) and (trie.contains('care') == True), "Error on test_delete_existing_word_with_more_letters_left"


def test_delete_non_existing_word():
    with pytest.raises(Exception):
        expected = Exception('The word does no exist.')

        trie = Trie()
        word = 'car'
        actual = trie.delete(word)

        assert actual == expected, 'Error on test_delete_non_existing_word.'


def test_words_from_prefix_one(trie__with_words):
    prefix = "car"
    expected = ['car', 'care', 'careful', 'card']

    actual = trie__with_words.get_words_from_prefix(prefix)

    assert actual == expected, 'Error on test_words_from_prefix_one.'


def test_words_from_prefix_two(trie__with_words):
    prefix = "e"
    expected = ['egg']

    actual = trie__with_words.get_words_from_prefix(prefix)

    assert actual == expected, 'Error on test_words_from_prefix_two.'


def test_words_from_prefix_two(trie__with_words):
    prefix = "no"
    expected = ['nothing', 'notice']

    actual = trie__with_words.get_words_from_prefix(prefix)

    assert actual == expected, 'Error on test_words_from_prefix_two.'


def test_words_from_prefix_empty_prefix(trie__with_words):
    prefix = ""
    expected = []

    actual = trie__with_words.get_words_from_prefix(prefix)

    assert actual == expected, 'Error on test_words_from_prefix_empty_prefix.'


def test_words_from_prefix_none_prefix(trie__with_words):
    prefix = None
    expected = []

    actual = trie__with_words.get_words_from_prefix(prefix)

    assert actual == expected, 'Error on test_words_from_prefix_none_prefix.'



def test_words_from_prefix_non_existing(trie__with_words):
    prefix = "x"
    expected = []

    actual = trie__with_words.get_words_from_prefix(prefix)

    assert actual == expected, 'Error on test_words_from_prefix_non_existing.'


def test_get_all_words(trie__with_words):
    expected = ['car', 'care', 'careful', 'card', 'egg', 'nothing', 'notice']

    actual = trie__with_words.get_all_words()

    assert actual == expected, 'Error on test_get_all_words.'


def test_get_all_words_empty():
    expected = []

    actual =  Trie().get_all_words()

    assert actual == expected, 'Error on test_get_all_words_empty.'

@pytest.fixture
def trie__with_words():
    trie = Trie()
    trie.insert("car")
    trie.insert("care")
    trie.insert("card")
    trie.insert("egg")
    trie.insert("nothing")
    trie.insert("careful")
    trie.insert("notice")

    return trie
