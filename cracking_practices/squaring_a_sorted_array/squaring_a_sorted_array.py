# Squaring a Sorted Array
# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]

def make_squares(arr):
    squares = []
    for i in range(len(arr)):
        squeared = arr[i] * arr[i]

        # if the squares is empty, just append it
        if len(squares) == 0 or squeared >= squares[-1]:
            squares.append(squeared)
            continue

        #   check where to insert
        #  if squared > last value (position 0) in the array, add it to the beggining
        if squeared <= squares[0]:
            squares.insert(0, squeared)
            continue

        # find its place somewhere in the middle of the array
        # I know the possitions can't be 0 or -1
        j = 1
        while j < len(squares):
            # check if there I can add it
            if squares[j] == squeared:
                squares.insert(j, squeared)
                break

            #  before moving ahead, I will check if the next value>squeared. (I will never check in a non existing value in this case)
            if squares[j+1] > squeared:
                squares.insert(j+1, squeared)
                break

            j += 1

    return squares
