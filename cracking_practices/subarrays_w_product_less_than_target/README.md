[Table of Contents](../../README.md)

# Problem Subarrays with Product Less than a Target

<!-- [Whiteboard approach](subarrays_w_product_less_than_target) -->

### PROBLEM DOMAIN
Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.

### VISUALS

```
Example 1:

Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Example 2:
Input: [8, 2, 6, 5], target=50
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
Explanation: There are seven contiguous subarrays whose product is less than the target.
```

### EDGE CASES
-   I can assume I will have unique possitive numbers.

### ALGORITHMS

#### APPROACH 1, Sliding window.

```
create a function that receives an array and a target
    declare variables

    traverse the array using sliding window approach
        check if my current pointers are less than target, if so, append it to result

        check if the product is < target

        move the window 1 space to the right


        check if I need to shrink the window, if product > target
            shrink

            get the current product


    return result

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I only need to traverse the array once.

**Space O(n):** Worst case, my return array can have the same len of my input array.

### CODE

[cracking_practices/subarrays_w_product_less_than_target/subarrays_w_product_less_than_target.py](subarrays_w_product_less_than_target.py)

### TESTS

[tests/test_subarrays_w_product_less_than_target.py](../../tests/test_subarrays_w_product_less_than_target.py)

### GITHUB BRANCH

[Pull Request # 56, Branch: subarrays_w_product_less_than_target](https://github.com/ilealm/cracking-practices/pull/56)
