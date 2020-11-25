# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

# I will have 3 pointers, then I will check if the sum of them is 0, if so, then I will move
def search_triplets(arr):
    # sort the array so I can have the convinations in order
    arr.sort()
    triplets = []

    current = 0
    runner1 = 1
    runner2 = 2
    while current <= len(arr) - 3:

        # move runner1
        for i in range(runner1, len(arr) - 1):
            for j in range(runner2, len(arr)):
                if arr[current] + arr[i] + arr[j] == 0:
                    # THIS WILL ADD AAAALLLLL THE EXISTING CONVINATIONS
                    # triplets.append([arr[current], arr[i], arr[j]])
                    # BUT the problem wants unique triplets, I will check if is not already there
                    founded = [arr[current], arr[i], arr[j]]

                    if not founded in triplets:
                        triplets.append(founded)

        runner2 += 1
        runner1 += 1
        current += 1

    return triplets


