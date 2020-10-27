[Table of Contents](../../README.md)


# Problem Longest Subarray with Ones after Replacement

### PROBLEM DOMAIN
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.


### VISUALS
```
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
```

### EDGE CASES
- The array only will have 1 | 0 values.
- K is an integer > 0.
- Array can be n lenght.


### ALGORITHMS

#### APPROACH 1, Sliding window
```
create a funcion length_of_longest_substring that receives (arr, k):
    declare helper funcions
    replacements = 0
    max_lenght = 0
    pointer_left = 0

    add basic validations to input

    traverse all the array, where current position is pointer_right

        if current position is 0
            if I still have replacements available:
                replacements += 1
            else :
                save max
                I need to add one more replacement for the current pointer_right
                I need to shirk the window until the replacements are available again
                create a loop while I have reach replacements <= k
                    check if the possition I'm shirinking is a replacement, if so, substract from replacements
                    move the window 1 space


    # check if the latest window is the longest.

    return max_lenght
```


#### TESTS
```
Please review the test section below.
```


#### BIG O
**Time O(n):** I need to traverse once all the elements in the array.
**Space O(1):** I'm using the same DS for any N size.

### CODE
[cracking_practices/longest_subsrt_w_1s_replacement/longest_subsrt_w_1s_replacement.py](longest_subsrt_w_1s_replacement.py)


### TESTS
[tests/test_longest_subsrt_w_1s_replacement.py](../../tests/test_longest_subsrt_w_1s_replacement.py)

### GITHUB BRANCH

[Pull Request # 44, Branch: longest_subsrt_w_1s_replacement](https://github.com/ilealm/cracking-practices/pull/44)
