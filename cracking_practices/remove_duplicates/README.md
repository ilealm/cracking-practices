[Table of Contents](../../README.md)

# Problem Remove Duplicates

<!-- [Whiteboard approach](remove_duplicates) -->

### PROBLEM DOMAIN
 Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

### VISUALS

```
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
```

### EDGE CASES
- The array will be sorted.
- The array will have only numbers.

### ALGORITHMS

#### APPROACH, 2 pointers, one is a runner.

```
    declare a function remove_duplicates which receives an array
    set vaable runner = 0

    create a loop for all the array
        increase runner by 1

        create a while runner < len(arr) and arr[runner] == arr[pointer_left]
            if true, pop that possition
            arr.pop(runner)

    return len(arr)
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse only one the array.

**Space O(1):** I don't need extra space.

### CODE

[cracking_practices/remove_duplicates/remove_duplicates.py](remove_duplicates.py)

### TESTS

[tests/test_remove_duplicates.py](../../tests/test_remove_duplicates.py)

### GITHUB BRANCH

[Pull Request # 51, Branch: remove_duplicates](https://github.com/ilealm/cracking-practices/pull/51)
