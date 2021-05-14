# Function that search in list for a value using binary search.
# If the value is found, then the value's index in return
# If the value is not found, then returns -1
def binary_search(array, value_to_find):
    print(array)
    # stablish my left and right pointers
    left = 0
    right = len(array) - 1
    while left <= right:
        # get the middle of my array
        middle = (left + right) // 2
        # compare if middle is the value I'm looking for, if is, return it
        if array[middle] == value_to_find:
            return middle
        # if not, check if I need to move to left or right and move pointers
        if value_to_find < array[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1

