[Table of Contents](../../README.md)


# Problem

<!-- [Whiteboard approach](X) -->

### PROBLEM DOMAIN
Given a string and a pattern, find all anagrams of the pattern in the given string.


### VISUALS
```
Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
```

### EDGE CASES
- I can asume the string won't be empty.


### ALGORITHMS

#### APPROACH Sliding window
```
add basic validations
create a dictionary for the Pattern
create return_array
create pointers, left =0, right = len(pattern)

use a while to use sliding window method to move thought the string. this while will be until right < len(string)
    for each window i will tranform into a dict, then compare if both dict are equal, if so, append value to array.
    move window: increase by one left and right

return return_array
```


#### TESTS
```
Please review the test section below.
```


#### BIG O
**Time O(n):** In worst case scenario, I need to traverse all the possitions.

**Space O(n):** I need to create dicionaries, and in worst case scneario both have each character.

### CODE
[cracking_practices/string_anagrams/string_anagrams.py](string_anagrams.py)


### TESTS
[tests/test_string_anagrams.py](../../tests/test_string_anagrams.py)

### GITHUB BRANCH

[Pull Request # 47, Branch: string_anagrams](https://github.com/ilealm/cracking-practices/pull/47)
