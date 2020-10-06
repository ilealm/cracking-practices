[Table of Contents](../../README.md)


# Problem Smallest Subarray with a given sum

<!-- [Whiteboard approach](X) -->

### PROBLEM DOMAIN
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.

### VISUALS
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].


Example 2:
Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].


Example 3:
Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

### EDGE CASES
- Array can be N length.
- Return 0, if no such subarray exists.
- The sum can not exist.

### ALGORITHMS

#### APPROACH 1
```
create a function that acepts an array and S
    add basic validation to array
    declare variables
    import math module

    create a loop for all the array
        add to window_sum the value of array[right_ponter]
        increase window_count by one

        shrink array if I hit the value S
        while window_sum is equal or grater than S:
            obtain the min counter using min function
            decrease the window
            substract window_sum le left pointer
            increase by one left_pointer

    return 0 if smallest_count == math.inf else smallest_count
```


#### TESTS
```
please review tests.
```


#### BIG O
**Time O(n):** I need to traverse all the array, then the while again, processes only once, which is n*n => n
**Space O(1):** I'm always using the same variables.

### CODE
[cracking_practices/smallest_subarray/smallest_subarray.py](smallest_subarray.py)


### TESTS
[tests/test_smallest_subarray.py](../../tests/test_smallest_subarray.py)

### GITHUB BRANCH

[Pull Request # 37, Branch: smallest_subarray](https://github.com/ilealm/cracking-practices/pull/37)
