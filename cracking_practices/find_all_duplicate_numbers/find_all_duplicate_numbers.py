# Find all Duplicate Numbers
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
# The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.


def cycle_sort(nums):
    i = 0
    while i < len(nums):
        jump = nums[i] - 1

        if nums[i] == nums[jump]:
            i += 1
        else:
            nums[i], nums[jump] = nums[jump], nums[i]



def find_all_duplicates(nums):
    duplicateNumbers = []
    cycle_sort(nums)
    print(nums)
    for i in range(len(nums)):
        if not nums[i] -1 == i:
            duplicateNumbers.append(nums[i])

    # i need to sort so the return array is equal to the test. Educative doesn't need this.
    duplicateNumbers.sort()
    return duplicateNumbers





if __name__ == "__main__":
#     print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))

