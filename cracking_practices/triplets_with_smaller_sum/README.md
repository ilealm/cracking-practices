[Table of Contents](../../README.md)

# Problem Triplets with Smaller Sum

<!-- [Whiteboard approach](triplets_with_smaller_sum) -->

### PROBLEM DOMAIN
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

### VISUALS

```
Example 1:
Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Example 2:
Input: [-1, 4, 2, 1, 3], target=5
Output: 4
Explanation: There are four triplets whose sum is less than the target:
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
```

### EDGE CASES

- I can assume I will have only numbers.
- I can asume the array will have more than 3 elements.

### ALGORITHMS

#### APPROACH 1,

```
create a function that receives an array and target
    declare a counter count = 0
    # I really don't need to sort the list, but I will do it to have the same output arrays as the examples
    # it would be helpful to sort if I need to end in some point, but in this case I need to check all the
    # possibles triplests
    arr.sort()

    set left = 0

    create a while from left to len(arr) - 2:
        create a loop i in range( left + 1, len(arr) - 1):
            create a loop j in range( i + 1, len(arr)):
                obtain current_sum
                compare if current_sum < target, if so, count += 1


        left += 1


    return count

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n^2):** Because I have nested loops to create all the triplets.

**Space O(n):** I'm only creating the same DS regardless the input.

### CODE

[cracking_practices/triplets_with_smaller_sum/triplets_with_smaller_sum.py](triplets_with_smaller_sum.py)

### TESTS

[tests/test_triplets_with_smaller_sum.py](../../tests/test_triplets_with_smaller_sum.py)

### GITHUB BRANCH

[Pull Request # 54, Branch: triplets_with_smaller_sum](https://github.com/ilealm/cracking-practices/pull/54)
