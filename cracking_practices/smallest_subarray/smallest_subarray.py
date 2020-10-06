# Smallest Subarray with a given sum
# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray
# whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# Example 1:
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

# Example 2:
# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# Example 3:
# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
import math

# Approach 1
def smallest_subarray_v1(array, S):
    window_sum = window_count = left_pointer = 0
    smallest_count = len(array)
    founded = False

    for right_ponter in range(len(array)):
        window_sum += array[right_ponter]
        window_count += 1
        if window_sum >= S:
            # assign a variable to let know if I founded
            if not founded : founded = True

            # I will shrik the window to test all the values before right_pointer, BC I could have there the value
            while left_pointer < right_ponter:
                if window_sum >= S:
                    if window_count < smallest_count:
                        smallest_count = window_count
                # slide window
                window_sum -= array[left_pointer]
                window_count -= 1
                left_pointer += 1

    if array[-1] >= S:
        return 1

    return 0 if not founded else smallest_count




# Approach 2
def smallest_subarray(array, S):
    window_sum = window_count = left_pointer = 0
    smallest_count = math.inf

    for right_ponter in range(len(array)):
        window_sum += array[right_ponter]
        window_count += 1

        while window_sum >= S:
            smallest_count = min(smallest_count, window_count)
            window_count -= 1
            window_sum -= array[left_pointer]
            left_pointer += 1

    return 0 if smallest_count == math.inf else smallest_count


