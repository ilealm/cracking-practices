# Given a unsorted list, return the same list in an ordered fashion, implementing Selection Sort.

def selection_sort(array):
    # sablish my left pointer
    current_index = 0

    # traverse all the array from current_index+1, to find the min value
    while current_index < len(array):
        # I need to stablish on each round, the new min
        min_value_index = current_index
        min_value = array[min_value_index]
        # traversing_index is the inner runner, which always starts ar current_index + 1
        traversing_index = current_index + 1
        while traversing_index < len(array):
        # if I use a for, the index will be not the same as the array, thats why I need to use another while and a traversing_index
            # check if where I'm is the new min, if so, set new min values
            if array[traversing_index] < min_value:
                min_value = array[traversing_index]
                min_value_index = traversing_index
            traversing_index += 1

        # swap the values from my current_index to the new min
        array[current_index], array[min_value_index] = array[min_value_index], array[current_index]
        # move to the next index
        current_index += 1
    return array





