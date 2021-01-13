# Find the Missing Number
# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

# Helper function that sort in place the numbers STARTING AT 0.
def cycle_sort(nums):
    i = 0
    n = len(nums) # so I just calculate this once
    while i < n:
        jump = nums[i]
        # I need to check if jump < n BC if not, I will pass my array length. In the next loops I will acomodate this values
        if jump < n and not nums[i] == nums[jump]:
            # swap
            nums[i], nums[jump] = nums[jump], nums[i]
        else:
            i += 1


def find_missing_number(nums):

    cycle_sort(nums)

    for i in range(len(nums)):
        # if the value is not the same as index, means the number is missing
        if not nums[i] == i:
            return i
