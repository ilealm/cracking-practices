[Table of Contents](../../README.md)

# Problem Triplet Sum Close to Target

<!-- [Whiteboard approach](triplet_sum_close_to_target) -->

### PROBLEM DOMAIN
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as
close to the target number as possible, return the sum of the triplet. If there are more than one such
triplet, return the sum of the triplet with the smallest sum.

### VISUALS

```
Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
```

### EDGE CASES

- I will have an array with more than 3 positions.

### ALGORITHMS

#### APPROACH 1, 2 pointers

```
declare function  triplet_sum_close_to_target(arr, target_sum):
    sort the array so I can have the convinations in order
    arr.sort()
    set closest_value = math.inf and  sum_closet_value = 0

    current = 0
    runner1 = 1

    iterate through all the array
        move runner1
        get a triplet
        current_sum = (arr[current] + arr[current + 1] + arr[current + 2])
                get the distance from current sum to target
                distance = abs(abs(target_sum) - current_sum)

                if distance < closest_value :
                    closest_value = distance
                    sum_closet_value = current_sum

        move pointers

    return sum_closet_value

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(N^2)** For the sort and the nested fors.

**Space O(1):** I'm not creating new DS for this challenge.

### CODE

[cracking_practices/triplet_sum_close_to_target/triplet_sum_close_to_target.py](triplet_sum_close_to_target.py)

### TESTS

[tests/test_triplet_sum_close_to_target.py](../../tests/test_triplet_sum_close_to_target.py)

### GITHUB BRANCH

[Pull Request # 54, Branch: triplet_sum_close_to_target](https://github.com/ilealm/cracking-practices/pull/54)
