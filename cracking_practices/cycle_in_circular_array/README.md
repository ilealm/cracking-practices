[Table of Contents](../../README.md)

# Problem Cycle in a Circular Array


### PROBLEM DOMAIN
We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

### VISUALS

```
Input: [1, 2, -1, 2, 2]
Output: true

Example 2:
Input: [2, 2, -1, 2]
Output: true

Example 3:
Input: [2, 1, -1, -2]
Output: false
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, Implementing fast and slow pointers.

```
Logic based on idea of: https://www.youtube.com/watch?v=2hVinjU-5SA

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the elements in the array.

**Space O(1):** I'm not creating new DS thanks to fast and slow pointers.

### CODE

[cracking_practices/cycle_in_circular_array/cycle_in_circular_array.py](cycle_in_circular_array.py)

### TESTS

[tests/test_cycle_in_circular_array.py](../../tests/test_cycle_in_circular_array.py)

### GITHUB BRANCH

[Pull Request # 69, Branch: cycle_in_circular_array](https://github.com/ilealm/cracking-practices/pull/69)
