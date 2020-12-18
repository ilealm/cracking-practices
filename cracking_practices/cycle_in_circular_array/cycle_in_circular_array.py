# Cycle in a Circular Array
# We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

# If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
# If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

# Logic based on idea of: https://www.youtube.com/watch?v=2hVinjU-5SA



# I will use a faster and slowe pointers to find the loop in thge array.
def circular_array_loop_exists(arr):

    if len(arr)<2 : return False

    # because i can have a loop at any position of the array, I will loop in all of them or when I found a loop
    for i in range(len(arr)):
        slower = faster = i


        # I need to know if all the loop will be forward or backwards
        moving_forward = arr[i] > 0

        while True:
            # move pointers. Slower 1 position, Faster 2 positions of their value
            slower = get_next_position(arr, slower, moving_forward)
            if slower == -1:
                break

            faster = get_next_position(arr, faster, moving_forward)
            if faster == -1:
                break

            # do next jump
            faster = get_next_position(arr, faster, moving_forward)
            if faster == -1:
                break


            # check if I have a loop
            if slower == faster :
                return True

    return False



def get_next_position(arr, index, moving_forward):
    # check if I still moving in the same direction
    current_direction = arr[index] > 0

    # if my current index points to a different direction than my moving_forward, I should brake the cycle.
    if not current_direction == moving_forward:
        return -1

    # obtain the next index, which will be the jump from index + value of arr[index].
    # I will use % to create a cycle
    jump_to = (index + arr[index]) % len(arr)

    if jump_to < 0:
        jump_to += len(arr)

    # if I'm pointing to the index, this means that the loop is only 1 position lenght
    if (jump_to == index):
        return -1

    return jump_to


