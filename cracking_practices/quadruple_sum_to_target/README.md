[Table of Contents](../../README.md)

# Problem Quadruple Sum to Target

<!-- [Whiteboard approach](quadruple_sum_to_target) -->

### PROBLEM DOMAIN
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

### VISUALS

```
Example 1:
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

Example 2:
Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.

```

### EDGE CASES

- I can have only numbers, and the array will have values.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, Nested loops one ahead of the other to create the combinations.

```
    create a function that receives an array and a target
    not requiered step, but I will do it so the problem pass the test: sort the array


   Because I need to generate all the combinations, I will traverse the array
   with 4 nested loops because I need to find combinations of 4 elements
    # level 1
    for l1 in range(len(arr)-3):
        # level 2
        for l2 in range(l1+1, len(arr)-2):
            # level 3
            for l3 in range(l2+1, len(arr)-1):
                # level 4
                for l4 in range(l3+1, len(arr)):
                    if sum of all pointers == target:
                        create a temporary array with the combination of all pointers
                        I'm going to sort the array so the resuls are in the same order as the challenge
                        temp_array = [arr[l1], arr[l2], arr[l3], arr[l4]]
                        temp_array.sort()
                        BS I can have duplicated values, I need to check If I don't aready have the combination.
                        if is not in the array, append temp_array to return array
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n^2):** I need to have nested loops.

**Space O(n):** I can have a bigger return array as the input.

### CODE

[cracking_practices/quadruple_sum_to_target/quadruple_sum_to_target.py](quadruple_sum_to_target.py)

### TESTS

[tests/test_quadruple_sum_to_target.py](../../tests/test_quadruple_sum_to_target.py)

### GITHUB BRANCH

[Pull Request # 58, Branch: quadruple_sum_to_target](https://github.com/ilealm/cracking-practices/pull/58)
