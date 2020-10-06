# PROBLEM DOMAIN
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3]


def max_sub_array(array, K):
    if K > len(array):
        return -1

    left_pointer = window_sum = maximum = 0

    # start traversing all the array
    for right_pointer in range(len(array)):
        window_sum += array[right_pointer]

        # check if I already reach the K element. When I reach it, then I can do windows slides.
        if right_pointer >= K - 1:
            # check if I have a new max
            if window_sum > maximum:
                maximum = window_sum
            # start the window sliding
            # #1 :remove the value of the left
            window_sum -= array[left_pointer]
            # #2: slide window 1 possition
            left_pointer += 1

    return maximum



