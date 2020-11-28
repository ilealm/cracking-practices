# Triplets with Smaller Sum
# Given an array arr of unsorted numbers and a target sum, count all triplets in it such
# that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
# Write a function to return the count of such triplets.

def triplet_with_smaller_sum(arr, target):
    count = 0
    # I really don't need to sort the list, but I will do it to have the same output arrays as the examples
    # it would be helpful to sort if I need to end in some point, but in this case I need to check all the
    # possibles triplests
    arr.sort()

    left = 0


    while left <= len(arr) - 2:
        for i in range( left + 1, len(arr) - 1):
            for j in range( i + 1, len(arr)):
                current_sum = arr[left] + arr[i] + arr[j]
                if current_sum < target : count += 1

        left += 1


    return count


