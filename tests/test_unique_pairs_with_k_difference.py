import pytest
from cracking_practices.unique_pairs_with_k_difference.unique_pairs_with_k_difference import GetUniquePairsCount



def test_empty_list():
    # my_list = [1, 7, 5, 9, 2, 12, 3]
    my_list = []
    k = 2
    pairs = GetUniquePairsCount(my_list, k)

    assert pairs.get_num_unique_pairs() == 0



def test_must_return_4():
    my_list = [1, 7, 5, 9, 2, 12, 3]
    k = 2
    pairs = GetUniquePairsCount(my_list, k)

    assert pairs.get_num_unique_pairs() == 4



def test_must_return_4():
    my_list = [1, 1, 1, 10, 2, 12, 3]
    k = 2
    pairs = GetUniquePairsCount(my_list, k)

    assert pairs.get_num_unique_pairs() == 2
