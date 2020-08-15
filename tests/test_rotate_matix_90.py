import pytest
from cracking_practices.rotate_matix_90.rotate_matix_90 import rotate_matix_90_new_matrix

def test_rotate_matix_90_new_matrix_one():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    actual = rotate_matix_90_new_matrix(matrix)

    assert actual == expected, "Error on test_rotate_matix_90_new_matrix_one."


def test_rotate_matix_90_new_matrix_two():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    expected = [
        [3, 1],
        [4, 2]
    ]

    actual = rotate_matix_90_new_matrix(matrix)

    assert actual == expected, "Error on test_rotate_matix_90_new_matrix_two."


def test_rotate_matix_90_new_matrix_three():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    expected = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]

    actual = rotate_matix_90_new_matrix(matrix)

    assert actual == expected, "Error on def test_rotate_matix_90_new_matrix_three."
