# import pytest
# from cracking_practices.find_first_k_missing_positive.find_first_k_missing_positive import find_first_k_missing_positive

import pytest
from cracking_practices.find_first_k_missing_positive.find_first_k_missing_positive import find_first_k_missing_positive

def test_one():
    array = [3, -1, 4, 5, 5]
    k = 3

    expected = [1, 2, 6]

    actual = find_first_k_missing_positive(array, k)

    assert actual == expected, 'Error on test_one.'



def test_two():
    array = [-2, -3, 4]
    k = 2

    expected = [1, 2]

    actual = find_first_k_missing_positive(array, k)

    assert actual == expected, 'Error on test_two.'
