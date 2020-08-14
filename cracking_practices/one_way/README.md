[Table of Contents](../../README.md)


# Problem 1.5 : One Away

[Whiteboard approach](https://docs.google.com/document/d/1HtRG_kvD-4p0eHq7OyvYLRgEab5ealwQYyHM2B4Pdrg/edit?usp=sharing)

### PROBLEM DOMAIN
There are three types of edits that can be performed on strings: insert a character,  remove a character, or replace a character. Given two strings,  write a function to check if they are one edit or zero edits away. Return true or false.

### VISUALS
```
INPUT					OUTPUT
sale, sales				True
dale, pale				True
midle, middle			True
abcde, abcde			False
abcde, edcba			False
```


### EDGE CASES
- The base word will be the first input, and the second input will be the word to review.
- Words can be any length.
- The second input has only one edition.



### ALGORITHMS

#### APPROACH1: Brute force, compare scenario by scenario.

```
create a function that receives two inputs
   # compare original_word to compare_word, if are equal, return false
   if compare_word is equal original_word:
       return False

   # check if there is a missing letter, in the beginning or end
   if len(compare_word) is equal to len(original_word) -1:
       # check if the 1st letter is the only one different
       if original_word[1:] is equal compare_word:
           return True

       # check if the last letter is the only one different
       if original_word[:-1] is equal to compare_word:
           print('deleted last letter')
           return True

       # check if there is a missing letter in the middle
       create a lopp from 0 to len(original_word)-1):
           if not original_word[i] is equal to compare_word[i]:
               if original_word[i+1:] is equal to compare_word[i:]:
                   return True

   # compare_word is bigger to original_word by one, if so, then check is an insert
   if len(original_word) + 1 is equal to len(compare_word):
       create a loop from 0 to  len(original_word)-1):
           if not original_word[i] is equal to compare_word[i]:
               if original_word[i:] is equal to compare_word[i+1:]:
                   return True

       # check last letter
       if original_word == compare_word[:-1]:
           return True

   # check if there is a upd letter
   if len(compare_word) is equal to len(original_word):
       # compare each letter, if there is not equal, comprare the rest of the string
       for i in range(0, len(original_word)-1):
           if not original_word[i] == compare_word[i]:
               if original_word[i+1:] == compare_word[i+1:]:
                   return True

   return False, is not of any of the past conditions meet

```


#### TESTS
_Please review Whiteboard approach_
```
TEST
inputs (sale, sales)

checks
original_word = sale
compare_word = sales  True

original_word = sale
compare_word = dale

original_word = midddle
compare_word = middle

```


#### BIG O
**Time O(n):** I'm traversing on worst scenario only input one.


**Space O(n):** I'm not creating new ds.

### CODE
[cracking_practices/one_way/one_way.py](one_way.py)


### TESTS
[tests/test_x.py](../../tests/test_one_way.py)

### GITHUB BRANCH

[Pull Request # 9, Branch: one_way](https://github.com/ilealm/cracking-practices/pull/9)
