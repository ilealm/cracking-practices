import pytest
from cracking_practices.rotate_matix_90.rotate_matix_90 import rotate_matix_90_new_matrix, rotate_matix_90_in_place


# NEW MATRIX TESTS
def test_rotate_matix_90_new_matrix_empty():
    matrix = []
    expected = []

    actual = rotate_matix_90_new_matrix(matrix)

    assert actual == expected, "Error on test_rotate_matix_90_new_matrix_empty."


def test_rotate_matix_90_new_matrix_2by2(matrix_2by2):
    expected = [
        [3, 1],
        [4, 2]
    ]

    actual = rotate_matix_90_new_matrix(matrix_2by2)

    assert actual == expected, "Error on test_rotate_matix_90_new_matrix_2by2."


def test_rotate_matix_90_new_matrix_3by3(matrix_3by3):
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    actual = rotate_matix_90_new_matrix(matrix_3by3)

    assert actual == expected, "Error on test_rotate_matix_90_new_matrix_3by3."


def test_rotate_matix_90_new_matrix_4by4(matrix_4by4):
    expected = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]

    actual = rotate_matix_90_new_matrix(matrix_4by4)

    assert actual == expected, "Error on def test_rotate_matix_90_new_matrix_4by4."


def test_rotate_matix_90_new_matrix_5by5(matrix_5by5):
    expected = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]

    actual = rotate_matix_90_new_matrix(matrix_5by5)

    assert actual == expected, "Error on def test_rotate_matix_90_new_matrix_5by5."



# IN PLACE TESTS
def test_rotate_matix_90_in_place_empty():
    matrix = []
    expected = []

    actual = rotate_matix_90_in_place(matrix)

    assert actual == expected, "Error on test_rotate_matix_90_in_place_empty."


def test_rotate_matix_90_in_place_2by2(matrix_2by2):
    expected = [
        [3, 1],
        [4, 2]
    ]

    actual = rotate_matix_90_in_place(matrix_2by2)

    assert actual == expected, "Error on test_rotate_matix_90_in_place_2by2."


def test_rotate_matix_90_in_place_3by3(matrix_3by3):
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    actual = rotate_matix_90_in_place(matrix_3by3)

    assert actual == expected, "Error on test_rotate_matix_90_in_place_3by3."


def test_rotate_matix_90_in_place_4by4(matrix_4by4):
    expected = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]

    actual = rotate_matix_90_in_place(matrix_4by4)

    assert actual == expected, "Error on def test_rotate_matix_90_in_place_4by4."


def test_rotate_matix_90_in_place_5by5(matrix_5by5):
    expected = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]

    actual = rotate_matix_90_in_place(matrix_5by5)

    assert actual == expected, "Error on def test_rotate_matix_90_in_place_5by5."


@pytest.fixture
def matrix_2by2():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    return matrix


@pytest.fixture
def matrix_3by3():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    return matrix

@pytest.fixture
def matrix_4by4():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    return matrix

@pytest.fixture
def matrix_5by5():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8 , 9 ,10],
        [11,12, 13, 14, 15],
        [16, 17, 18, 19,20],
        [21, 22, 23, 24,25],
    ]
    return matrix

# [21, 16, 11, 6, 1]
# [22, 17, 12, 7, 2]
# [23, 18, 13, 8, 3]
# [24, 19, 14, 9, 4]
# [25, 20, 15, 10, 5]
