

def quick_sort(array, left, right):


    if left >= right:
        return

    pivot_index = partition(array, left, right)

    if left < pivot_index - 1:  # this if helps to exit the recursion
        quick_sort(array, left, pivot_index-1)
    if pivot_index < right:
        quick_sort(array, pivot_index, right)

    return array





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
        # if array[left] < array[right]:
        if left < right:
            array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    return left


if __name__ == "__main__":
    # test = [19, 220, 63, 105, 2, 46, 50] # works
    test = [19, 220, 63, 105, 2, 46] # dont works
    # test = [19, 22, 63, 105, 2, 46]
    # test = [10, 15, -3, 12, 1, 30, 7]
    print (quick_sort(test, 0, len(test)-1))
    # quick_sort(test, 0, len(test)-1)
    # print (quick_sort_craking(test, 0, len(test)-1))
    # print (test)
