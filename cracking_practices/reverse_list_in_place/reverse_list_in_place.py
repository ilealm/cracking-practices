# Function that receives a list and return the same list but with the elements in inverted order.

def reverse_list_in_place(array):
    # if len(array) <= 1, there is nothing to swap.
    if len(array) <= 1: return array

    # declare left and right pointer
    left = 0
    right = len(array) - 1

    # create a loop while left<right and swap pointers
    while left < right:
        array[left], array[right] = array[right], array[left]
        # move left and right pointers 1 position closer
        left += 1
        right -= 1

    return array


