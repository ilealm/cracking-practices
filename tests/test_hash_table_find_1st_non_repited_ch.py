
import pytest
from cracking_practices.hash_table_find_1st_non_repited_ch.hash_table_find_1st_non_repited_ch import TextChecking


def test_empty_text():
    checker = TextChecking()
    text_to_check = ""
    first_non_repeted = checker.return_first_non_repeted(text_to_check)

    assert first_non_repeted == None


def test_return_g():
    checker = TextChecking()
    text_to_check = "A green apple."
    first_non_repeted = checker.return_first_non_repeted(text_to_check)

    assert first_non_repeted == "g"


def test_all_same_letters():
    # bbbbb => b
    checker = TextChecking()
    text_to_check = "bbbbBBBbbB"
    first_non_repeted = checker.return_first_non_repeted(text_to_check)

    assert first_non_repeted == "b"


def test_letters_and_numbers():
    # aa13d0s211 =>3
    checker = TextChecking()
    text_to_check = "aa13d0s211"
    first_non_repeted = checker.return_first_non_repeted(text_to_check)

    assert first_non_repeted == "3"


def test_text_with_spaces():
    checker = TextChecking()
    text_to_check = "aa1 3d0s211"
    first_non_repeted = checker.return_first_non_repeted(text_to_check)

    assert first_non_repeted == " "




# from cracking_practices.hash_table_find_1st_non_repited_ch.hash_table_find_1st_non_repited_ch import BLANK, HashTable


# def test_create_HashTable():
#     assert HashTable(size=10) is not None


# def test_HashTable_size():
#     assert len(HashTable(0)) == 0
#     assert len(HashTable(10)) == 10
#     assert len(HashTable(100)) == 100
#     assert len(HashTable(30)) == 30


# def test_HashFuntion_always_return_same_index():
#     HH_10 = HashTable(10)
#     key = "ten"
#     index = HH_10.__get_index__(key)
#     assert index == HH_10.__get_index__(key)

#     HH_10 = HashTable(10)
#     key = "five"
#     index = HH_10.__get_index__(key)
#     assert index == HH_10.__get_index__(key)

#     HH_100 = HashTable(100)
#     key = "one_hundred"
#     index = HH_100.__get_index__(key)
#     assert index == HH_100.__get_index__(key)

#     HH_50 = HashTable(50)
#     key = "fifhty"
#     index = HH_50.__get_index__(key)
#     assert index == HH_50.__get_index__(key)

#     HH_50 = HashTable(50)
#     key = "ten"
#     index = HH_50.__get_index__(key)
#     assert index == HH_50.__get_index__(key)




# def test_HashTable_insert_key_value_pairs():
#     HH = HashTable(10)
#     key = "hello"
#     value = "hola"

#     HH.add(key, value)

#     assert HH.is_key_in_table(key)
#     assert not HH.is_key_in_table("__empty__1234")



# def test_HashTable_retrieve_value_by_key():
#     HH = HashTable(10)
#     key = "today"
#     value = "hoy"
#     HH.add(key,value)
#     assert HH.get_value(key) == "hoy"

#     key = "nine"
#     value = "nueve"
#     HH.add(key,value)
#     assert HH.get_value(key) == "nueve"



# def test_HashTable_remove_item():
#     HH = HashTable(10)
#     key = "today"
#     value = "hoy"
#     HH.add(key,value)

#     assert HH.get_value(key) == 'hoy'
#     HH.delete('key')
#     # assert HH.get_value(key) is BLANK

