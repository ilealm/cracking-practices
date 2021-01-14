[Table of Contents](../../README.md)

# Problem Find the Duplicate Number

<!-- [Whiteboard approach](find_duplicate_number) -->

### PROBLEM DOMAIN
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

### VISUALS

```
Example 1:
Input: [1, 4, 4, 3, 2]
Output: 4

Example 2:
Input: [2, 1, 3, 3, 5, 4]
Output: 3

Example 3:
Input: [2, 4, 1, 4, 4]
Output: 4

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- 0 is not present in the array.
- Can't use extra space.

### ALGORITHMS

#### APPROACH 1, Cycle sort and return the values that are not in its correct place.

```
Sort the array in cycle sort manner.
Loop the array and return the value that is different from index, this means that if is out of order is the dupplicated, in this case. (Could also be a missing value)

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the array.

**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/find_duplicate_number/find_duplicate_number.py](find_duplicate_number.py)

### TESTS

[tests/test_find_duplicate_number.py](../../tests/test_find_duplicate_number.py)

### GITHUB BRANCH

[Pull Request # 80, Branch: find_duplicate_number](https://github.com/ilealm/cracking-practices/pull/80)
