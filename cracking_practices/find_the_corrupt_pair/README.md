[Table of Contents](../../README.md)

# Problem Find the Corrupt Pair

### PROBLEM DOMAIN
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

### VISUALS

```
Example 1:
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Example 2:
Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- Only positive numbers.
- 0 is not in the list.

### ALGORITHMS

#### APPROACH 1, Cycle Sort

```
Sort the array using sort cycle.
Sort the array and return the values that are not at its current position.

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the array.

**Space O(1):** I'm not creating any new DS.

### CODE

[cracking_practices/find_the_corrupt_pair/find_the_corrupt_pair.py](find_the_corrupt_pair.py)

### TESTS

[tests/test_find_the_corrupt_pair.py](../../tests/test_find_the_corrupt_pair.py)

### GITHUB BRANCH

[Pull Request # 82, Branch: find_the_corrupt_pair](https://github.com/ilealm/cracking-practices/pull/82)
