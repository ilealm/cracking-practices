# PROBLEM DOMAIN
# Rotate Matix - 1.7: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees.

# APPROACH 1, Brute approach, Create a new matrix and traverse using 2 loops.
def rotate_matix_90_new_matrix(matrix):
    n = len(matrix)
    return_matrix = []
    for i in range(0,n):
        return_matrix.append([None] * n)

    # if n=3
    for row in range(0, n):
        for col in range(0, n):
            return_matrix[col][(n-1)-row] = matrix[row][col]

    return return_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print(rotate_matix_90_new_matrix(matrix))
