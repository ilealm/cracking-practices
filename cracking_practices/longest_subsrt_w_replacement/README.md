[Table of Contents](../../README.md)


# Problem Longest Substring with Same Letters after Replacement

### PROBLEM DOMAIN
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

### VISUALS
```
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".


Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
```

### EDGE CASES
- The word can be any lenght.
- I can assume I will receive only lower case letters.
- K will be an integer not None.


### ALGORITHMS

#### APPROACH 1, Sliding window with a inner runner.
```
declare a function that receives a string an a integer k value.
    declare pointer_left = 0
    declare replacements = 0 to have count of replacements made.
    deckare max_str = '' to save the longest substring so far.

    traverse the string from 1 to end, using pointer_right as variable
        if pointer_right is different than pointer_left:
            If I still have replacements available, I will count one more
                replacements += 1
            else:
                save max
                here I reached k replacements, so I need to shrink the window to the begining of the replacements
                shrink my window from left by 1
                set my runner to 1 ahead left
                reset replacements
                create a while runnner <= pointer_right

                    if pointer_right is different than pointer_left:
                        If I still have replacements available, I will count one more
                            replacements += 1
                        else:
                            save max
                            shrink my window from left by 1
                    add 1 to runner

        check if my current window > max, if so, stablish new max

    return len(max_str)
```


#### TESTS
```
Please review the test section below.
```


#### BIG O
**Time O(n):** I need to traverse all the positions and I don't have inner loops.

**Space O(1):** I'm creating the same DS.

### CODE
[cracking_practices/longest_subsrt_w_replacement/longest_subsrt_w_replacement.py](longest_subsrt_w_replacement.py)


### TESTS
[tests/test_longest_subsrt_w_replacement.py](../../tests/test_longest_subsrt_w_replacement.py)

### GITHUB BRANCH

[Pull Request # 43, Branch: longest_subsrt_w_replacement](https://github.com/ilealm/cracking-practices/pull/43)
