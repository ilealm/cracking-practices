[Table of Contents](../../README.md)

# Problem Words Concatenation

<!-- [Whiteboard approach](words_concatenation) -->

### PROBLEM DOMAIN
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

### VISUALS

```
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:
Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
```

### EDGE CASES

- It is given that all words are of the same length.
- I can assume I will reveive valid data.


### ALGORITHMS

#### APPROACH 1, Sliding window.

```
create a helper function that returns the number of character in all the array


create find_word_concatenation which receives a str and array (words)
    declare variables result_indices, pointer_left

    obtain the number of characters in all the array words
    create a loop for len(str)
        if my current window is the same size of all my words
        # I have to say pointer_right +1 so I can INCLUDE that chr (which is the current)
            declare a flag variable and set to true
            ckech if all the words in the array exist in the current window
            if all the words exist in the window, append pointer left to result_indices

            regardless if the words are in the array, I shirnk the window 1 possition

   return result_indices
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n*m):** Where m is array. I need to traverse all the characters in the string, and then check all the words in the words array.
**Space O(n):** I'm creating an array that can varies depending on N.

### CODE

[cracking_practices/words_concatenation/words_concatenation.py](words_concatenation.py)

### TESTS

[tests/test_words_concatenation.py](../../tests/test_words_concatenation.py)

### GITHUB BRANCH

[Pull Request # 49, Branch: words_concatenation](https://github.com/ilealm/cracking-practices/pull/49)
