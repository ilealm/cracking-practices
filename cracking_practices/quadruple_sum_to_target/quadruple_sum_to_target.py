# Quadruple Sum to Target
# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

# Example 1:
# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.

# Example 2:
# Input: [2, 0, -1, 1, -2, 2], target=2
# Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
# Explanation: Both the quadruplets add up to the target.


def search_quadruplets(arr, target):
    quadruplets = []
    # not requiered step, but I will do it so the problem pass the test.
    # arr.sort

    # Because I need to generate all the combinations, I will traverse the array
    # with 4 nested loops because I need to find combinations of 4 elements
    # level 1
    for l1 in range(len(arr)-3):
        # level 2
        for l2 in range(l1+1, len(arr)-2):
            # level 3
            for l3 in range(l2+1, len(arr)-1):
                # level 4
                for l4 in range(l3+1, len(arr)):
                    if arr[l1] + arr[l2] + arr[l3] + arr[l4] == target:
                        # I'm going to sort the array so the resuls are in the same order as the challenge
                        temp_array = [arr[l1], arr[l2], arr[l3], arr[l4]]
                        temp_array.sort()
                        # BS I can have duplicated values, I need to check If I don't aready have the combination.
                        if not temp_array in quadruplets:
                            quadruplets.append(temp_array)


    return quadruplets

