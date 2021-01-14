[Table of Contents](../../README.md)

# Problem Find all Missing Numbers

### PROBLEM DOMAIN
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.


### VISUALS

```
Example 1:
Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Example 2:
Input: [2, 4, 1, 2]
Output: 3

Example 3:
Input: [2, 3, 2, 1]
Output: 4

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- Array doesn't have 0 number.

### ALGORITHMS

#### APPROACH 1, Cycle Sort

```
Step 1: Sort the array using cycling sort.
Step 2: Loop the array and return the values that are not the same as its index - 1.

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the array.

**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/find_all_missing_numbers/find_all_missing_numbers.py](find_all_missing_numbers.py)

### TESTS

[tests/test_find_all_missing_numbers.py](../../tests/test_find_all_missing_numbers.py)

### GITHUB BRANCH

[Pull Request # 77, Branch: find_all_missing_numbers](https://github.com/ilealm/cracking-practices/pull/77)
