[Table of Contents](../../README.md)


# Problem Smallest Window containing Substring

<!-- [Whiteboard approach](smallest_containing_substrig) -->

### PROBLEM DOMAIN
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

### VISUALS
```
Example 1:
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:
Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
```

### EDGE CASES
- I can asumme I will receive valid values.


### ALGORITHMS

#### APPROACH 1, Sliding window, using sets.
```
create a function that receives a string and a pattern

    create a set of the pattern, which I will check if exist inside my current window
    create pointers for the window
    shrik my window from str to the inner characters

    check if my pattern is a subset of my current window
        if so, get smallest value
        move pointer_left += 1

    return value
```


#### TESTS
```
Please review the test section below.
```


#### BIG O
**Time O(n):** I need to traverse all the string.

**Space O(1):** I'm using the same variables regardless the N size.

### CODE
[cracking_practices/smallest_containing_substrig/smallest_containing_substrig.py](smallest_containing_substrig.py)


### TESTS
[tests/test_smallest_containing_substrig.py](../../tests/test_smallest_containing_substrig.py)

### GITHUB BRANCH

[Pull Request # 48, Branch: smallest_containing_substrig](https://github.com/ilealm/cracking-practices/pull/48)
