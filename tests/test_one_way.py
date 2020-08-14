import pytest
from cracking_practices.one_way.one_way import one_way



def test_empty_words():
    # check if the 1st letter is the only one different
    original_word = 'abcde'
    compare_word = ''
    expected = False

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_empty_words."

def test_empty_words_two():
    # check if the 1st letter is the only one different
    original_word = ''
    compare_word = 'abcde'
    expected = False

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_empty_words_two."

def test_same_words():
    # check if the 1st letter is the only one different
    original_word = 'abcde'
    compare_word = 'abcde'
    expected = False

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_same_words."


def test_same_letters_dff_order():
    # check if the 1st letter is the only one different
    original_word = 'abcde'
    compare_word = 'ebcda'
    expected = False

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_same_words."


def test_1st_letter_is_diff_one():
    # check if the 1st letter is the only one different
    original_word = 'pale'
    compare_word = 'ale'
    expected = True

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_1st_letter_is_diff_one."

def test_1st_letter_is_diff_two():
    # check if the 1st letter is the only one different
    original_word = 'pale'
    compare_word = 'sale'
    expected = True

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_1st_letter_is_diff_two."


def test_last_letter_is_diff_one():
    # check if the 1st letter is the only one different
    original_word = 'sale'
    compare_word = 'sales'
    expected = True

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_last_letter_is_diff_one."


def test_last_letter_is_diff_two():
    # check if the 1st letter is the only one different
    original_word = 'sale'
    compare_word = 'sal'
    expected = True

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_last_letter_is_diff_two."


def test_middle_letter_instert():
    # check if the 1st letter is the only one different
    original_word = 'midle'
    compare_word = 'middle'
    expected = True

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_middle_letter_instert."

def test_middle_letter_delete():
    # check if the 1st letter is the only one different
    original_word = 'middle'
    compare_word = 'midle'
    expected = True

    actual = one_way(original_word, compare_word)

    assert actual == expected, "Error on test_middle_letter_delete."


