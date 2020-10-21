[Table of Contents](../../README.md)


# Problem: No Repeat Substring

<!-- [Whiteboard approach](X) -->

### PROBLEM DOMAIN
Given a string, find the length of the longest substring which has no repeating characters.

### VISUALS
```
Example 1:
Input: String="aabccbb"
Output: 3

Example 2:
Input: String="abbbb"
Output: 2

Example 3:
Input: String="abccde"
Output: 3
```

### EDGE CASES
- The word can be empty.
- Is case sensitive.
- Any character is allowed.


### ALGORITHMS

#### APPROACH 1, Sliding Window
```
# I will keep a window with all diferent chrs, and on each addition to the window
# I will review which is the max lenght.
def no_repeat_substring(str):
    if len(str) == 0 : return 0

    pointer_left = 0
    max_chr_counter = 0
    for pointer_right in range(1, len(str)):
        if len(str[pointer_left:pointer_right]) > max_chr_counter :
            max_chr_counter = len(str[pointer_left:pointer_right])

        #  check uf my current value is in my window, if so, I will shirnk it one possition from left.
        while str[pointer_right] in str[pointer_left : pointer_right] and pointer_left < pointer_right:
            pointer_left += 1


    return max_chr_counter
```

#### APPROACH 2, Using variables
```
def no_repeat_substring(str):
    # have 2 variables: sub_string and max_sub_string
    # traverse all the str comparing each letter.
    # if current letter not in sub_string, add it. Else set max_sub_string, reset sub_string
    # return len(max_sub_string)
    if len(str) == 0 : return 0
    sub_string = max_sub_string = ''

    for pointer in range(len(str)):
        if str[pointer] in sub_string:
            # I found a duplicate, so I'm going to reset sub_string, but before I will store the current max_sub_string
            if len(sub_string) > len(max_sub_string) :
                max_sub_string = sub_string
            sub_string = ''

        sub_string += str[pointer]

    return len(max_sub_string)

```


#### TESTS
```
Please review the test secion below.
```


#### BIG O
**Time O(n):** I need to traverse all the input word.

**Space O(1):** I'm using the same variables for everycase.

### CODE
[cracking_practices/no_repeat_substring/no_repeat_substring.py](no_repeat_substring.py)


### TESTS
[tests/test_no_repeat_substring.py](../../tests/test_no_repeat_substring.py)

### GITHUB BRANCH

[Pull Request # 42, Branch: no_repeat_substring](https://github.com/ilealm/cracking-practices/pull/42)


