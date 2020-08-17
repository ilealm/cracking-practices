# PROBLEM DOMAIN
# Rotate Matix - 1.7: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees.

# APPROACH 1, Brute approach, Create a new matrix and traverse using 2 loops.
def rotate_matix_90_new_matrix(matrix):
    n = len(matrix)
    return_matrix = []
    for i in range(0, n):
        return_matrix.append([None] * n)

    # if n=3
    for row in range(0, n):
        for col in range(0, n):
            return_matrix[col][(n - 1) - row] = matrix[row][col]

    return return_matrix


def rotate_matix_90_in_place(matrix):
    n = len(matrix)

    for row in range(0, n // 2):
        for col in range(row, n-row-1):
            # save the current value to replace right_top at the end of the steps
            top = matrix[row][col]
            # step 1 assign left_top to the current value of left_bottom
            matrix[row][col] = matrix[n - 1 - col][row]

            # step 2 move right_bottom to left_bottom here
            matrix[n - 1 - col][row] = matrix[n - row- 1][n - 1 - row- col]

            # step 3 move right_top to right_bottom
            matrix[n - row- 1][n - 1- row- col] = matrix[col][n - row- 1]

            # step 4 move left_top to right_top
            matrix[col][n - row - 1] = top

    return matrix




if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]

    x = rotate_matix_90_in_place(matrix)
    for i in range(0,len(x)):
        print(x[i])
    # print(rotate_matix_90_new_matrix(matrix))

