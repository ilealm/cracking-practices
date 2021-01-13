# Cyclic Sort
# We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on
# their creation sequence. This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space. For simplicity,
# let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

def cyclic_sort(nums):
    # Add basic validations
    if len(nums) == 0 : return nums

    pointer_left = 0

    while pointer_left < len(nums):
        # swap_pointer is the place where pointer_left will swap, and is -1 BC arrays starts at 0.
        swap_pointer = nums[pointer_left] - 1
        # ckeck if the value of pointer_left is in the right place, in this case, when both are pointing to the same spot.
        # if nums[pointer_left] == nums[swap_pointer]:
        if pointer_left == swap_pointer:
            # this value is in its right place, so I move the pointer_left
            pointer_left += 1
        else:
            # I need to swap the value of pointer_left with the value of swap_pointer
            nums[pointer_left], nums[swap_pointer] = nums[swap_pointer], nums[pointer_left]


    return nums

