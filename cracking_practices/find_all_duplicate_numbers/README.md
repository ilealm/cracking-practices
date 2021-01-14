[Table of Contents](../../README.md)

# Problem Find all Duplicate Numbers


### PROBLEM DOMAIN
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.

### VISUALS

```
Example 1:
Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Example 2:
Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, Cycle sort

```
Apply cycle sort
Loop all the input array and ppend to return array all the values that are different to its index.

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the array once.

**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/find_all_duplicate_numbers/find_all_duplicate_numbers.py](find_all_duplicate_numbers.py)

### TESTS

[tests/test_find_all_duplicate_numbers.py](../../tests/test_find_all_duplicate_numbers.py)

### GITHUB BRANCH

[Pull Request # 81, Branch: find_all_duplicate_numbers](https://github.com/ilealm/cracking-practices/pull/81)
