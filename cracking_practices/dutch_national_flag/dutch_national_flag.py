# array = [2, 2, 0, 1, 2, 0

# expected = [0 0 1 2 2 2 ]

import math
# I will traverse all the array, and on each position I will search for the smallest of the list, and keep its position,
# then if founded, I will swap positions with current i
def dutch_flag_sort(arr):
    smallest = math.inf
    smallest_pos = 0

    for i in range(len(arr)):
        # find the smallest
        for s in range(i, len(arr)):
            if arr[s] < smallest:
                smallest = arr[s]
                smallest_pos = s

        # now I will check if I need to swap values
        if smallest < arr[i]:
            arr[i], arr[smallest_pos] = arr[smallest_pos], arr[i]

        # reset smallest fo the next round
        smallest = math.inf

    return arr


