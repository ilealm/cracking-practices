[Table of Contents](../../README.md)

# Problem Happy Number
<!-- [Whiteboard approach](happy_number) -->

### PROBLEM DOMAIN
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the
square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

### VISUALS

```

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, Converting to string. (Not implementing 2 pointers)

```
    obtain the sum of all the digits^2 in the current number


    ckeck if current_sum == 1, if so,     return True

    store the current sum
        if not current_sum already stored
            append to the list
            establish the new number to compare
        else:
            if I already got this number, means it will never be 1

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(logN):** I need to traverse the number M times depenging on my input.

**Space O(n):** I'm creating a new array that could be size n.

### CODE

[cracking_practices/happy_number/happy_number.py](happy_number.py)

### TESTS

[tests/test_happy_number.py](../../tests/test_happy_number.py)

### GITHUB BRANCH

[Pull Request # 64, Branch: happy_number](https://github.com/ilealm/cracking-practices/pull/64)
