# array = [1, 2, 3, 4, 6]
# target = 6
# expected = [1, 3]


# approach two pointers using a flag to know which pointer to move. This will work also for NOT SORTED arrays
def pair_with_targetsumV1(arr, target_sum):
    arr_return = []
    # add basic validations
    if arr == [] or target_sum <= 0:
        return arr_return

    # declare two pointers, one to left and other to rigth
    pointer_left = 0
    pointer_right = len(arr) - 1
    # declare a flag variable to move 1 pointer at a time in the while
    move_right = True

    # lopp thru all the array until pointers meet at the middle, or I found a pair
    while pointer_left < pointer_right and pointer_right >= pointer_left:
        # check if sum of my pointers == target
        if arr[pointer_left] + arr[pointer_right] == target_sum:
            arr_return.append(pointer_left)
            arr_return.append(pointer_right)
            break

        # I need to move 1 pointer at a time, so I can compare it in the next loop
        if move_right:
            pointer_right -= 1
        else:
            pointer_left += 1

        # change flag
        move_right = not move_right

    # return the array
    return arr_return


# same idea, clearer code
# this version is based on educative algorithm
def pair_with_targetsum(arr, target_sum):
    arr_return = []
    pointer_left = 0
    pointer_right = len(arr) - 1

    while pointer_left < pointer_right:
        current_sum = arr[pointer_left] + arr[pointer_right]

        if current_sum == target_sum:
            arr_return.append(pointer_left)
            arr_return.append(pointer_right)
            break

        # BC this array IS SORTED, i can implement this:
        # if my current_sum is bigger than my target_sum, then I will move right, because I know I need smallest
        # numbers to add. Otherwise, I wil move left BC I need bigger numbers.
        if current_sum > target_sum:
            pointer_right -= 1
        else:
            pointer_left += 1


    return arr_return

