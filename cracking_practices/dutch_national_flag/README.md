[Table of Contents](../../README.md)

# Problem

<!-- [Whiteboard approach](dutch_national_flag) -->

### PROBLEM DOMAIN

### VISUALS

```
Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Example 2:
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
```

### EDGE CASES

-  I can have only 0, 1 and 2 values.

### ALGORITHMS

#### APPROACH 1, finding smallest

```
I will traverse all the array, and on each position I will search for the smallest of the list, and keep its position,
then if founded, I will swap positions with current i

        find the smallest
        now I will check if I need to swap values
        reset smallest fo the next round
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(nLogN):** I need to check the smallest in all the loops.

**Space O(1):** I'm not creating new ds.

### CODE

[cracking_practices/dutch_national_flag/dutch_national_flag.py](dutch_national_flag.py)

### TESTS

[tests/test_dutch_national_flag.py](../../tests/test_dutch_national_flag.py)

### GITHUB BRANCH

[Pull Request # 57, Branch: dutch_national_flag](https://github.com/ilealm/cracking-practices/pull/57)
