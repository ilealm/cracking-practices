# Problem Statement #
# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# Example 2:
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']


def fruits_into_baskets(fruits):
    if fruits == [] : return 0

    current_fruits = set()
    sub_fruits = ''

    for right_pointer in range(len(fruits)):
        sub_fruits += fruits[right_pointer]

        # I'm changing tree, and I aleady have 2 types in my basquets
        if not fruits[right_pointer] in current_fruits:
            if len(current_fruits) >= 2:
                # I'm going to remove the oldest tree
                sub_fruits = sub_fruits[1:]
                # recreate the current fruits
                current_fruits = set(sub_fruits)
            else:
                current_fruits.add(fruits[right_pointer])


    return len(sub_fruits)


