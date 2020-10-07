[Table of Contents](../../README.md)


# Problem Maximum Sum Subarray of Size K

<!-- [Whiteboard approach](X) -->

### PROBLEM DOMAIN
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

### VISUALS
```
Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
```

### EDGE CASES
- X


### ALGORITHMS
- Array of positive numbers.
- Positive number ‘k’.
- K can be greater than the length of the array.
- Array can be empty.

#### APPROACH Sliding Window.
```
declare a function max_sub_array that receives an array and K
    add basic validations to the input

    set variables
    left_pointer = window_sum = maximum = 0

    start traversing all the array using a for to len(array))
        window_sum += array[right_pointer]

        check if I already reach the K element. When I reach it, then I can do windows slides.
        if right_pointer >= K - 1:
            check if I have a new max
            start the window sliding:
            #1 :remove the value of the left
            #2: slide window 1 possition

    return maximum

```


#### TESTS
```
please review test secction
```


#### BIG O
**Time O(n):** I only need to traverse the array once.

**Space O(1):** I'm using the same variables all the time.

### CODE
[cracking_practices/max_sub_array/max_sub_array.py](max_sub_array.py)


### TESTS
[tests/test_max_sub_array.py](../../tests/test_max_sub_array.py)

### GITHUB BRANCH

[Pull Request # 36, Branch: max_sub_array](https://github.com/ilealm/cracking-practices/pull/36)
