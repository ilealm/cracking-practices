[Table of Contents](../../README.md)

# Problem

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN
Given an array of integers, count the number of unique pairs of integers that have difference k.

### VISUALS

```
Input: [1, 7, 5, 9, 2, 12, 3] K=2
Output: 4

We have four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9).
Note that we only want the number of these pairs, not the pairs themselves.

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1,

```
Create the pairs permutations.
If each permutation has k difference, add it to an array, if it's not already there.

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n2):** I need to traverse the array 2 times, the second inside the first to create the permutations/

**Space O(n):** I'm creating a new list to save the pairs.

### CODE

[cracking_practices/unique_pairs_with_k_difference/unique_pairs_with_k_difference.py](unique_pairs_with_k_difference.py)

### TESTS

[tests/test_unique_pairs_with_k_difference.py](../../tests/test_unique_pairs_with_k_difference.py)

### GITHUB BRANCH

[Pull Request # 104, Branch: unique_pairs_with_k_difference](https://github.com/ilealm/cracking-practices/pull/104)
