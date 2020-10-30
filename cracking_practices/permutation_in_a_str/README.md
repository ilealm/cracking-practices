[Table of Contents](../../README.md)


# Problem Permutation in a String

<!-- [Whiteboard approach](X) -->

### PROBLEM DOMAIN
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string.


### VISUALS
```
Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
```

### EDGE CASES
- Inputs can be any lenght.
- Inputs can be empty.
- Inputs can be any character.


### ALGORITHMS

#### APPROACH 1, Sliding window, and implement dictionaries
```
add basic validations
create a dictionary for the Pattern
create pointers, left =0, right = len(pattern)

use a while to use sliding window method to move thought the string. this while will be until right < len(string)
    for each window i will tranform into a dict, then compare if both dict are equal, if so, return true
    move window: increase by one left and right

```


#### TESTS
```
Please review the test section below.
```


#### BIG O
**Time O(n):** In worst case scenario, I need to traverse all the possitions.

**Space O(n):** I need to create dicionaries, and in worst case scneario both have each character.

### CODE
[cracking_practices/permutation_in_a_str/permutation_in_a_str.py](permutation_in_a_str.py)


### TESTS
[tests/test_permutation_in_a_str.py](../../tests/test_permutation_in_a_str.py)

### GITHUB BRANCH

[Pull Request # 45, Branch: permutation_in_a_str](https://github.com/ilealm/cracking-practices/pull/45)
