[Table of Contents](../../README.md)

# Problem Pair with Target Sum

<!-- [Whiteboard approach](pair_with_target_sum) -->

### PROBLEM DOMAIN
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target. Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

### VISUALS

```

```

### EDGE CASES

-   I can assume I will receive valid input.

### ALGORITHMS

#### APPROACH 1, Two pointers

```
    approach two pointers using a flag to know which pointer to move. This will work also for NOT SORTED arrays
    declare two pointers, one to left and other to rigth
    pointer_left = 0
    pointer_right = len(arr) - 1
    declare a flag variable to move 1 pointer at a time in the while
    move_right = True

    lopp thru all the array until pointers meet at the middle, or I found a pair
    while pointer_left < pointer_right and pointer_right >= pointer_left:
        check if sum of my pointers == target

        I need to move 1 pointer at a time, so I can compare it in the next loop
        change flag

    return the array
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the array only once.

**Space O(1):** I'm not creating new ds.

### CODE

[cracking_practices/pair_with_target_sum/pair_with_target_sum.py](pair_with_target_sum.py)

### TESTS

[tests/test_pair_with_target_sum.py](../../tests/test_pair_with_target_sum.py)

### GITHUB BRANCH

[Pull Request # 50, Branch: pair_with_target_sum](https://github.com/ilealm/cracking-practices/pull/50)
