# This solution is based on the example ofthe book Grokking Algorithms, By Aditya Y. Bhargava.
# The AMAZING part of this code is the implementation of list comprenhension to get the less and greaters values
# from the pivot (insted of a partition function, that the most of the books does)
# And still implements recursion.


def quick_sort(array):
    # my base case is where I don't have anything to sort
    if len(array) < 2:
        return array

    # the pivot will be the index 0
    pivot = array[0]

    # using list comprehension I gill get all the values min and max from the pivot.
    # I need to say array[1:] BC the 0 is the pivot and I'n not considering it
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    print(less + [pivot] + greater)
    # returning in this way, I'm sending the array in a sorted way
    return quick_sort(less) + [pivot] + quick_sort(greater)
