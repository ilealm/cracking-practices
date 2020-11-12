import pytest
from cracking_practices.pair_with_target_sum.pair_with_target_sum import pair_with_targetsum

def test_one():
    array = [1, 2, 3, 4, 6]
    target = 6

    expected = [1, 3]

    actual = pair_with_targetsum(array, target)

    assert actual == expected, 'Error on test_one.'


def test_two():
    array = [2, 5, 9, 11]
    target = 11

    expected = [0, 2]

    actual = pair_with_targetsum(array, target)

    assert actual == expected, 'Error on test_two.'

if __name__ == "__main__":
    pass
