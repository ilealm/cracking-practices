# Given an array of sorted numbers, remove all duplicates from it.
# You should not use any extra space; after removing the duplicates
# in-place return the length of the subarray that has no duplicate in it.


# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].


def remove_duplicates(arr):
    runner = 0

    for pointer_left in range(len(arr)):
        runner += 1

        while runner < len(arr) and arr[runner] == arr[pointer_left]:
            arr.pop(runner)

    return len(arr)
