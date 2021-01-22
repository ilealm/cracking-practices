# Find the Corrupt Pair
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’,
# but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

# sort where nums DO NOT CONTAINS ZERO
def cycle_sort(nums):
    i = 0

    while i < len(nums):
        jump = nums[i] - 1

        if nums[jump] == nums[i]:
            i += 1
        else:
            nums[i], nums[jump] = nums[jump], nums[i]


def find_corrupt_numbers(nums):
    if len(nums) == 0:
        return [-1, -1]

    cycle_sort(nums)

    for i in range(len(nums)):
        if not (nums[i] - 1) == i:
            return([nums[i] , i + 1])

    return [-1, -1]


