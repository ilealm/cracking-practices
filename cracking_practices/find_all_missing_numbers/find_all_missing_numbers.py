# Find all Missing Numbers
# We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
# The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.


# helper function that sorts an array. This code assume the numbers starts at 1, AND IT HAVE DUPPLICATES

def cycle_sort(nums):
    i = 0
    help = [0,1,2,3,4,5,6,7]
    while i < len(nums):
        # Define the value of the cell to jump
        jump = nums[i] - 1
        # if i == jump:  THIS DON'T WORK FOR DUPPLICATED VALUES IN THE ARRAY!
        # I need to compare in this way, so repeted values that already in place got ignored and leave it where they are.
        if nums[i] == nums[jump]:
            # the value of nums[i] is at its correct place, so I move i
            i += 1
        else:
            # nums[i] is not at its correct place, so I need to swap values
            nums[i], nums[jump] = nums[jump], nums[i]


def find_missing_numbers(nums):
    missing_numbers = []
    # Step 1: sort the array using cycle_sort
    cycle_sort(nums)
    print(nums)
    # Step 2: append to missing_numbers the values that are not equal to its index.
    # this arrray DOESN'T contain 0.

    for i in range(len(nums)):
        if not (nums[i] - 1) == i:
            missing_numbers.append(i + 1)

    return missing_numbers


