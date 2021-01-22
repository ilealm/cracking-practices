# Find the Smallest Missing Positive Number
# Given an unsorted array containing numbers, find the smallest missing positive number in it.


def cycle_sort(nums):
    all_possitives = (sum(n < 0 for n in nums)) <= 0
    # print(all_possitives)
    # return
    i = 0
    while i < len(nums):
        jump = nums[i]
        if all_possitives:
            jump -= 1

        # validate if the number is negative, if so, put at index 0
        if jump < 0:
            nums[0], nums[i] = nums[i], nums[0]
            i += 1
        else:
            if jump >= len(nums):
                nums[i], nums[-1] = nums[-1], nums[i]
                i += 1
            else:
                if nums[i] == nums[jump]:
                    i += 1
                else:
                    nums[i], nums[jump] = nums[jump], nums[i]


def find_first_smallest_missing_positive(nums):
    if len(nums) == 0:
        return -1

    cycle_sort(nums)
    print(nums)
    if nums[0] < 0:
        for i in range(1,len(nums)):
            if not nums[i] == i:
                return i
    else:
        for i in range(len(nums)):
            if not nums[i] == i + 1:
                return i + 1


def find_first_smallest_missing_positive_educative(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(n):
    if nums[i] != i + 1:
      return i + 1

  return len(nums) + 1

# def main():
#   print(find_first_smallest_missing_positive_educative([-3, 1, 5, 4, 2]))
# #   print(find_first_smallest_missing_positive_educative([3, -2, 0, 1, 2]))
# #   print(find_first_smallest_missing_positive_educative([3, 2, 5, 1]))


# main()
