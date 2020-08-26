

def merge_sort(array):
    num_elements = len(array)
    if num_elements == 1 :
        return

    middle = num_elements // 2
    left = array[0:middle]
    right = array[middle:]

    
    merge_sort(left)
    merge_sort(right)


    merge_helves(left, right, array)

    return array

def merge_helves(left, right, array):

    right_pointer = 0
    left_pointer = 0
    array_pointer = 0
    while left_pointer <len(left) and right_pointer < len(right):
        if right[right_pointer] < left[left_pointer]:
            array[array_pointer] = right[right_pointer]
            right_pointer +=1
            array_pointer +=1
        else:
            array[array_pointer] = left[left_pointer]
            left_pointer += 1
            array_pointer += 1

    # add the elements that wasn't already added, from the left
    while left_pointer < len(left):
        array[array_pointer] = left[left_pointer]
        left_pointer += 1
        array_pointer += 1

    # add the elements that wasn't already added, from the right
    while right_pointer < len(right):
        array[array_pointer] = right[right_pointer]
        right_pointer += 1
        array_pointer += 1


if __name__ == "__main__":
    array = [30,25,15,41,5,80,40,1]
    print(array)
    print(merge_sort(array))
