# Find the Duplicate Number
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
# The array has only one duplicate but it can be repeated multiple times.
# Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.


def cycle_sort(nums):
    i = 0
    while i < len(nums):
        jump = nums[i] - 1

        if nums[i] == nums[jump]:
            i += 1
        else:
            nums[i], nums[jump] = nums[jump], nums[i]


def find_duplicate(nums):
    # step 1, sort the array in cycle sort manner
    cycle_sort(nums)
    print(nums)
    # step 2, to find the duplicated, is the one that is not at its right possition.
    for i in range(len(nums)):
        if not nums[i]-1 == i:
            return nums[i]
        prev = nums[i]

    return -1



