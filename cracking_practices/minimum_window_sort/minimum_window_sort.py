# Minimum Window Sort
# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# Example 2:

# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

import math

def shortest_window_sort(arr):
    # traverse all the array, and on each possition I will peek the next one.
    # if next < current, I will create a window from current until I find a bigger number than current
    # I will have a window_min, and check against previous_current, if window_min < previous_current, I will
    # grow my window 1 space to left.
    # save min

    # prev_current = math.inf
    current = 0
    smallest = math.inf

    left = 0
    min_window = math.inf
    right = 0

    while current < len(arr)-1 and current >= 0: # is -1 BC I use a peek

        # check if the next is < current
        # if arr[current] > arr[current+1]:
        if arr[current] > arr[current+1]:
            # I will create a window from current to a bigger number than current
            left = current
            right = current + 1

            # from this point I know is unsorted, so I need to find the maximous value in all the array
            # so later I can stabish the window
            max_value = arr[current]
            max_position = current
            for i in range(current+1, len(arr)):
                if arr[i] > max_value:
                    max_value = arr[i]
                    max_position = i

            # if I didn't found a bigger value means the array is sorted in reverse.
            if max_position == 0:
                smallest = len(arr)
                break

            right = max_position - 1

            if arr[left] < arr[right]:
                left -= 1

            # obtain the smallest
            smallest = min(smallest, len(arr[left:right]))

            # since I found a window, I will check the rest of the values BUT
            # from my current window, so I will move current to right
            current = right
        else:
            # move my current to the next position
            current += 1


    if smallest == math.inf :
        return 0
    else:
        return smallest



if __name__ == "__main__":
    # print(shortest_window_sort([ 1, 3, 2, 0, -1, 7, 10 ]))
    # print(shortest_window_sort([ 1, 2, 5, 3, 7, 10, 9, 12 ]))
    # print(shortest_window_sort([ 1, 2, 3 ]))
    print(shortest_window_sort([ 3, 2, 1 ]))


