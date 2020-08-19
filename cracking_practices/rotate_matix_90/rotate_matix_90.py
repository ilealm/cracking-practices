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


# APPROACH 2, Update un place.
# Viewing the matrix as a square, rotate the corners and then move one possition to the next cell.
def rotate_matix_90_in_place(matrix):
    n = len(matrix)

    # I will traverse until the middle (n//2) BC I'm updating from corners to certer
    for row in range(0,n//2):
        # Range start is on row to mantain a diagonal in the inner squares. (0,0; 1,1; 2,2...)
        # Range top has to be "n-1-row" BS the matrix is shrinking on each row loop, so I don't pass where I already passed.
        for col in range(row, n-1-row):
            # step 1, save top_left
            # top_left coordinates matrix[row][col]
            top_left = matrix[row][col]

            # step 2, replace:
            # top_left ----->  bottom_left
            # bottom_left coordinates = matrix[n-1-col][row]
            matrix[row][col] = matrix[n-1-col][row]

            # step 3, replace:
            # bottom_left -----> bottom_right
            # bottom_right coordinates matrix[n-1-row][n-1-col]
            matrix[n-1-col][row] = matrix[n-1-row][n-1-col]


            # step 4, replace:
            # bottom_right -----> top_right
            # top_right coordinates    matrix[col][n-1-row]
            matrix[n-1-row][n-1-col] = matrix[col][n-1-row]


            # step 5, replace:
            # top_right -----> top_left (saved value)
            matrix[col][n-1-row] = top_left

    return matrix





