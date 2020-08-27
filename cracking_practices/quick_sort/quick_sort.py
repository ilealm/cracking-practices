

def quick_sort(array, left, right):
    if left >= right:
        return

    pivot_index = partition(array, left, right)

    if left < pivot_index - 1:  # this if helps to exit the recursion
        quick_sort(array, left, pivot_index-1)
    if pivot_index < right:
        quick_sort(array, pivot_index, right)



    # return array
    return insertion_sort(array)





def partition(array, left, right):
    pivot = array[(left + right) // 2]

    #  move left and right until they meet each other
    while left <= right:
        # find the next value that are greater than pivot, starting from left
        while array[left] < pivot:
            left +=1

        # find the next value that are less than pivot, starting on right
        while array[right] > pivot:
            right -=1

        # swap left and right, if are in the reverse order
        if left < right:
            array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    return left



# This insertion and mergeSort code are not mine:
# Source https://www.educative.io/edpresso/what-is-the-best-sorting-algorithm-for-an-almost-sorted-array

# *************************
def insertion_sort(arr):
    # arr = [1, 2, 4, 3]
    for i in range(1, len(arr)):
        # Set key:
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            # Swap:
            arr[j + 1] = arr[j]
            arr[j] = key

            # Decrement 'j':
            j -= 1

    return arr

def mergeSort():
    myList = [1, 2, 4, 3]
    if len(myList) > 1:
        mid = len(myList) / 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1



# PROBLEM FOUND WITH MY quick_sort

# USING THIS ARRAY:
# test = [19, 220, 63, 105, 2, 46]
# [2, 19, 46, 105, 63, 220]
# The problem is that with the partitions, 63 don't get arraige, a very random error. I could use at the end a call to insertion_sort, which
# works better with almost ordered lists. But this add n time to the rutine. I could check at the end if the order is correct, but I also
# need to traverse all the list, so not sure if in this scenario is a good approach.

# The problem seems to be I'm using a middle partition. If I choose the beginning or end could fix this problem


# if __name__ == "__main__":
    # test = [19, 220, 63, 105, 2, 46] # dont works. The problem is that the first partition, 63 is send to the right and then never moves to its correct possition
    # print ('*****\n Original\n',test)
    # print (quick_sort(test, 0, len(test)-1))

    # test=[19, 220, 63, 105, 2, 46, 50]   # # dont works
    # print (quick_sort(test, 0, len(test)-1))

    # test=[5,75,3,4,87,26]   # # dont works
    # insertion_sort(test)
    # print (quick_sort(test, 0, len(test)-1))


    # insertion_sort(test)
    # print(test)
    # test = [19, 220, 63, 105, 2, 46, 50] # works

    # print ('*****\n Original\n',test)
    # print (quick_sort(test, 0, len(test)-1))

    # test = [19, 22, 63, 105, 2, 46, 500, 20, 150]  # dont works with out last call to insertion_sort
    # print (quick_sort(test, 0, len(test)-1))
