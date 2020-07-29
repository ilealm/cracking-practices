import pytest
from cracking_practices.linked_list.linked_list import LinkedList, Node


def test_LinkedList_one():
    actual = LinkedList()
    expected = None
    assert actual.head == expected

def test_LinkedList_two():
    ll = LinkedList()
    ll.insert("First")
    assert ll.head.value == "First"

def test_LinkedList_three(dummy_LinkedList):
    assert dummy_LinkedList.head.value == "Third"

def test_LinkedList_four(dummy_LinkedList):
    actual = dummy_LinkedList.includes("Five")
    assert actual == False

def test_LinkedList_five(dummy_LinkedList):
    actual = dummy_LinkedList.includes("First")
    assert actual


def test_LinkedList_six(dummy_LinkedList):
    actual = dummy_LinkedList.__str__()
    expected = "{ Third } -> { Second } -> { First } -> NULL"
    assert actual == expected

def test_LinkedList_six():
    ll = LinkedList()
    actual = ll.__str__()
    expected = "NULL"
    assert actual == expected

def test_append_one(dummy_LinkedList):
    dummy_LinkedList.append('Fourth')
    dummy_LinkedList.append('Fifth')
    actual = dummy_LinkedList.__str__()
    expected = "{ Third } -> { Second } -> { First } -> { Fourth } -> { Fifth } -> NULL"
    assert actual == expected


def test_insert_before_first_node():
    ll = LinkedList()
    ll.insert("First")
    ll.insert("Second")
    ll.insert_before("Second", "Third")
    actual = ll.__str__()
    expected = "{ Third } -> { Second } -> { First } -> NULL"
    assert actual == expected

def test_insert_before_middle():
    ll = LinkedList()
    ll.insert("First")
    ll.insert("Second")
    ll.insert_before("First", "1.5")
    actual = ll.__str__()
    expected = "{ Second } -> { 1.5 } -> { First } -> NULL"
    assert actual == expected

def test_insert_after_one(dummy_LinkedList):
    dummy_LinkedList.insert_after("Third", "Fourth")
    actual = dummy_LinkedList.__str__()
    expected = "{ Third } -> { Fourth } -> { Second } -> { First } -> NULL"
    assert actual == expected

def test_insert_after_head():
    ll = LinkedList()
    ll.insert("First")
    ll.insert_after("First", "Cero")
    actual = ll.__str__()
    expected = "{ First } -> { Cero } -> NULL"
    assert actual == expected

def test_insert_after_no_node():
    ll = LinkedList()
    ll.insert_after("One", "New value")
    actual = ll.__str__()
    expected = "NULL"
    assert actual == expected

def test_kth_from_end_greater(big_dummy_LinkedList):
    actual = big_dummy_LinkedList.kth_from_end(10)
    expected = "The kth position is greater than the Linkedlist lenght."
    assert actual == expected


def test_kth_from_end_same_lenght(big_dummy_LinkedList):
    actual = big_dummy_LinkedList.kth_from_end(6)
    expected = "Sixth"
    assert actual == expected

def test_kth_from_end_same_greater_cero(big_dummy_LinkedList):
    actual = big_dummy_LinkedList.kth_from_end(-5)
    expected = "The value to search must be greater than 0."
    assert actual == expected

def test_kth_from_end_one_node():
        ll = LinkedList()
        ll.insert("First")
        actual = ll.kth_from_end(1)
        expected = "First"
        assert actual == expected

def test_kth_from_end_same_greater_middle(big_dummy_LinkedList):
    actual = big_dummy_LinkedList.kth_from_end(4)
    expected = "Fourth"
    assert actual == expected




@pytest.fixture
def dummy_LinkedList():
    ll = LinkedList()
    ll.insert("First")
    ll.insert("Second")
    ll.insert("Third")
    return ll

@pytest.fixture
def big_dummy_LinkedList():
    ll = LinkedList()
    ll.insert("First")
    ll.insert("Second")
    ll.insert("Third")
    ll.insert("Fourth")
    ll.insert("Fifth")
    ll.insert("Sixth")
    return ll
