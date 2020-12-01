# Subarrays with Product Less than a Target
# Given an array with positive numbers and a target number, find all of its
# contiguous subarrays whose product is less than the target number.

# Input: [2, 5, 3, 10], target=30
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:

# Input: [8, 2, 6, 5], target=50
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
# Explanation: There are seven contiguous subarrays whose product is less than the target.


def find_subarrays(arr, target):
    result = []
    left = 0
    right = 1
    product = arr[left] * arr[right]

    # traverse the array using sliding window approach
    while left < right and right <= len(arr) -1:
        # check if my current pointers are less than target, if so, append it to result
        if arr[left] < target :
            if not [arr[left]] in result:
                result.append([arr[left]])

        if arr[right] < target :
            if not [arr[right]] in result:
                result.append([arr[right]])

        # check if the product is < target
        if product < target:
            result.append( arr[left:right+1] )

        # move the window 1 space to the right
        right += 1

        # check if I need to shrink the window, if product > target
        if right < len(arr):
            if product * arr[right] >= target:
                # shrink
                left += 1

            product = arr[left] * arr[right]


    return result

