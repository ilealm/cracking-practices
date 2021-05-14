from typing import NewType


def get_sum_all(array):
    # return sum(array)
    return sum(array, 1000)


# function that uses List comprehension to returns a new list where the elements contain 'a'
def get_fruits_with_a(fruits):
    newlist = [x for x in fruits if "a" in x]
    return newlist





# TESTING
# print(get_fruits_with_a(["apple", "banana", "cherry", "kiwi", "mango"]))
# print(get_sum_all(list(range(1,11))))
