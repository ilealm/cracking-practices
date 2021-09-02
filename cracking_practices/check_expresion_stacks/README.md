[Table of Contents](../../README.md)

# Problem

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN

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

#### APPROACH 1,

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

**Time O(n):** I need to

**Space O(n):** I'm

### CODE

[cracking_practices/x_x/x_x.py](x_x.py)

### TESTS

[tests/test_x_x.py](../../tests/test_x_x.py)

### GITHUB BRANCH

[Pull Request # n, Branch: x_x](https://github.com/ilealm/cracking-practices/pull/X)
