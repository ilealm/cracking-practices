# Triplet Sum Close to Target
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as
# close to the target number as possible, return the sum of the triplet. If there are more than one such
# triplet, return the sum of the triplet with the smallest sum.

# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

import math

def triplet_sum_close_to_target(arr, target_sum):
    # sort the array so I can have the convinations in order
    arr.sort()
    closest_value = math.inf
    sum_closet_value = 0

    current = 0
    runner1 = 1

    while current <= len(arr) - 3:

        # move runner1
        for i in range(runner1, len(arr) - 1):
            for j in range(runner1 + 1, len(arr)):
                # here, I have a triplet, so I will check if this value is the closest_value to target
                current_sum = (arr[current] + arr[i] + arr[j])
                # now, I will get the distance from current sum to target
                distance = abs(abs(target_sum) - current_sum)

                if distance < closest_value :
                    closest_value = distance
                    sum_closet_value = current_sum


        runner1 += 1
        current += 1

    return sum_closet_value



