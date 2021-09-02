[Table of Contents](../../README.md)

# Problem: Is a valid expresion?

<!-- [Whiteboard approach](check_expresion_stacks) -->

### PROBLEM DOMAIN
Given a expresion, return True if the opening tags "({<" has their closed tag in the right possition.


### VISUALS

```
(1+2)               : True
1+2)                : False
(1+2) <1>           : True
(1+2<) 1>           : False
(1+2) <1> - {5+9}   : True
(1+2)  {5+9 (7)     : False
```

### EDGE CASES

- Just check the right order odf the tags: (()[]{}<>)
- I don't need to check for logical syntax, I can have an empty <> or (1) and is valid.
- I can assume I'll only have numbers, tags and +,-,/,*
- I can have empty tags () + 1

### ALGORITHMS

#### APPROACH 1, Using Stacks with collections.deque

```
implement a stack object

create helper function that will return a boolean is the character is an opening one.
create helper function that will return a boolean is the character is a closing one.
create helper function that will return a boolean if the 2nd character is the closing one of the 1st character.
create a helper function to know if a character is not a tag (()[]{}<>)


Loop through every character.
    If the character is a opening tag:
        push it
    If the character is a closing tag:
        pop from the stack
        check is the poped character is the starting tag of the current character
            if not, return False

return true

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(1):** I need to pass the expresion only once.

**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/check_expresion_stacks/check_expresion_stacks.py](check_expresion_stacks.py)

### TESTS

[tests/test_check_expresion_stacks.py](../../tests/test_check_expresion_stacks.py)

### GITHUB BRANCH

[Pull Request # n, Branch: check_expresion_stacks](https://github.com/ilealm/cracking-practices/pull/94)
