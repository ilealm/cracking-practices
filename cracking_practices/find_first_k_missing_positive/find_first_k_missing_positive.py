# Find the First K Missing Positive Numbers
# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’
# missing positive numbers in the array.


def find_first_k_missing_positive(nums, k):
    # implement the same idea as educative
    n = len(nums)
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    # a way to store the values that are missing
    missingNumbers = []
    extraNumbers = set()
    for i in range(n):
        if len(missingNumbers) < k:
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)
                extraNumbers.add(nums[i])

    # check for the rest of the numbers
    i = 1
    while len(missingNumbers) < k:
        candidateNumber = i + n
        # ignore if the array contains the candidate number
        if candidateNumber not in extraNumbers:
            missingNumbers.append(candidateNumber)
            i += 1

    return missingNumbers


# def main():
#   print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
#   print(find_first_k_missing_positive([2, 3, 4], 3))
#   print(find_first_k_missing_positive([-2, -3, 4], 2))


# main()
