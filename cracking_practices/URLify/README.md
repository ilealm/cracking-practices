[Table of Contents](../../README.md)


# Problem 1.3 : URLify

[Whiteboard approach](https://docs.google.com/document/d/1HsC1SrnNspaUJQkMGgrBd0WueKyYt2xd9QFc08w8r4k/edit?usp=sharing)

### PROBLEM DOMAIN
URLify 1.3: Write a method to replace all the white spaces in a str_to_url with '%20'.
You may assume that the str_to_url has sufficient space at the end to hold the additional characters
and that you are given the true length of the str_to_url.

### VISUALS

Input : "Mr. John Smith    ",13

Output: "Mr.%20John%20Smith"


### EDGE CASES
- The change must be in place.
- The string will contain enough space to add the new characters.
- The string can not contain white spaces.
- The end of the string shouldn't finish with '%20'
- The length of the string doesn't include the last white spaces.
- Python doesn't accept string in place changes, because strings are immutable.

### ALGORITHMS

#### APPROACH 1,
PYTHON STYLE: I will create an empty return_string, and then traverse all the input string, if I found an empty space, I will add to return_string the substring '%20', else, I will add to return_string the current character.


```
declare a function URLify which acepts str_to_url and letters_count as parameters
   set variable URLify_string to ''
   remove empty spaces from beggining and end of the word
   loop all the input string
       if if current character is espace
           add to URLify_string '%20'
       else:
           add to URLify_string current character

   return URLify_string
```


#### TESTS
```
Input : "Mr. John Smith    ",13
str_to_url ="Mr. John Smith"
                          ^
URLify_string = M,Mr, Mr.,Mr.%20,Mr.%20J,Mr.%20Jo,,Mr.%20Jon,Mr.%20John, Mr.%20John%20, Mr.%20John%20S, Mr.%20John%20Sm, Mr.%20John%20Smi, Mr.%20John%20Smit, Mr.%20John%20Smith

```


#### BIG O
**Time O(n):** I need to traverse all the string.

**Space O(n):** I'm creating a new ds from almost the same length of the input.

### CODE
[cracking_practices/URLify/URLify.py](URLify.py)


### TESTS
[tests/test_URLify.py](../../tests/test_URLify.py)

### GITHUB BRANCH

[Pull Request # 8, Branch: URLify](https://github.com/ilealm/cracking-practices/pull/8)
