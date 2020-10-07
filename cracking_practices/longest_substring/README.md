[Table of Contents](../../README.md)


# Problem Longest Substring with K Distinct Characters

<!-- [Whiteboard approach](X) -->

### PROBLEM DOMAIN
Given a string, find the length of the longest substring in it with no more than K distinct characters.

### VISUALS
```
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
```

### EDGE CASES
- Can be N length.
- K must be a possitibe number.
- The input string can have any character.


### ALGORITHMS

#### APPROACH 1, Sliding window
```
create a function that receives a string and an integer
    declare variables

    loop all the array
        add letter to window_letters
        add window letters to set, which will avoid duplicates
        if len(dic) > k:
            stanlish new lontest
        if len(window_letters) > longest : set new longest
            remove[0] from window_letters
            reset set with new window_letters

    return longest
```


#### TESTS
```
Please review the test secion below.
```


#### BIG O
**Time O(n):** The outher loop runs for all characters, and the inner while process the characters only once, so O(n+n) => O(n)

**Space O(K):** Because I'm storing a maximoum of K elements in my set.

### CODE
[cracking_practices/longest_substring/longest_substring.py](longest_substring.py)


### TESTS
[tests/test_longest_substring.py](../../tests/test_longest_substring.py)

### GITHUB BRANCH

[Pull Request # 38, Branch: longest_substring](https://github.com/ilealm/cracking-practices/pull/38)
