

# Function that sums all the values in an array, using recursion
def recursion_sum(array):
    # base case
    if len(array) == 1:
        return(array[0])

    # on each recursion, I will send a 1 space smaller array
    return array[0] + recursion_sum(array[1:])



# Function that uses recursion to count the number of items in a list
def recursion_num_items(array):
    if array == [] : return 0

    # base case
    if len(array) == 1:
        return 1

    return 1 + recursion_num_items(array[1:])


# Function that finds the maximum value in an array using recursion
def recursion_find_max(array):

    if len(array) == 1:
        return array[0]
    current_max = array[0]

    return max(recursion_find_max(array[1:]), array[0])




def recursion_binary_search(array, target):
    if len(array) == 2:
        if array[0] == target:
            return array[0] # I found it, it was the last partition, so I send the index
        else:
            if array[1] == target:
                return array[1] # I found it, it was the last partition, so I send the index
            else:
                return -1 # the target is not in the list

    left = 0
    right = len(array) - 1
    middle = (left+right)//2
    if array[middle] == target:
        return array[middle]
    else:
        # call recursion, but check is im going to send the left or right part ot the array
        if target < array[middle]:
            right = middle # here I won't do -1, BC the slice is not inclusive [:right]
            return recursion_binary_search(array[left:middle], target)
        else:
            left = middle + 1 # here I won't do -1, BC the slice is not inclusive [:right]
            return recursion_binary_search(array[middle:], target)


