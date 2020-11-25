[Table of Contents](../../README.md)

# Problem Triplet Sum to Zero

<!-- [Whiteboard approach](triplet_sum_to_zero) -->

### PROBLEM DOMAIN
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

### VISUALS

```
Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
```

### EDGE CASES

-   I will have just numbers.

### ALGORITHMS

#### APPROACH 1,  using 3 pointers

```
I will have 3 pointers, then I will check if the sum of them is 0, if so, then I will move

sort the array so I can have the convinations in order

    check each sum of the pointers
    THIS WILL ADD AAAALLLLL THE EXISTING CONVINATIONS
    BUT the problem wants unique triplets, I will check if is not already there

    return triplets

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time   O(N^2)** For the sort and the nested fors.

**Space O(n):** For the returning array.

### CODE

[cracking_practices/triplet_sum_to_zero/triplet_sum_to_zero.py](triplet_sum_to_zero.py)

### TESTS

[tests/test_triplet_sum_to_zero.py](../../tests/test_triplet_sum_to_zero.py)

### GITHUB BRANCH

[Pull Request # 53, Branch: triplet_sum_to_zero](https://github.com/ilealm/cracking-practices/pull/53)
