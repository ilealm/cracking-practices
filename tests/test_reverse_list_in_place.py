import pytest
from cracking_practices.reverse_list_in_place.reverse_list_in_place import reverse_list_in_place


def test_five_elements():
    array=['a', 'b', 'c', 'd', 'e']

    expected =['e', 'd', 'c', 'b', 'a']

    actual = reverse_list_in_place(array)

    assert actual == expected, 'Error on test_five_elements.'



def test_empty_list():
    array=[]

    expected =[]

    actual = reverse_list_in_place(array)

    assert actual == expected, 'Error on test_empty_list.'


def test_even_list():
    array=['a', 'b', 'c', 'd', 'e','f']

    expected =['f', 'e', 'd', 'c', 'b', 'a']

    actual = reverse_list_in_place(array)

    assert actual == expected, 'Error on test_even_list.'


def test_numbers_list():
    array=[1,2,3,4,5,6,7,8,9,10]

    expected =[10,9,8,7,6,5,4,3,2,1]

    actual = reverse_list_in_place(array)

    assert actual == expected, 'Error on test_numbers_list.'



def test_one_element():
    array=['A']

    expected = ['A']

    actual = reverse_list_in_place(array)

    assert actual == expected, 'Error on test_one_element.'
