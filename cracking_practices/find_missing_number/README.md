[Table of Contents](../../README.md)

# Problem Find the Missing Number

### PROBLEM DOMAIN
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

### VISUALS

```
Input: [4, 0, 3, 1]
Output: 2

Example 2:
Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, Implement cycle sort and then return the number that is different as its index

```
def find_missing_number(nums):

    cycle_sort(nums)

    for i in range(len(nums)):
        # if the value is not the same as index, means the number is missing
        if not nums[i] == i:
            return i
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse the array once.

**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/find_missing_number/find_missing_number.py](find_missing_number.py)

### TESTS

[tests/test_find_missing_number.py](../../tests/test_find_missing_number.py)

### GITHUB BRANCH

[Pull Request # 77, Branch: find_missing_number](https://github.com/ilealm/cracking-practices/pull/77)
