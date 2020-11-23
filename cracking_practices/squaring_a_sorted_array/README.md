[Table of Contents](../../README.md)

# Problem Squaring a Sorted Array

<!-- [Whiteboard approach](squaring_a_sorted_array) -->

### PROBLEM DOMAIN
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

### VISUALS

```
Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]

```

### EDGE CASES
- I will have only numbers.
- I can have negative numbers.

### ALGORITHMS

#### APPROACH 1, comparing 0 and -1

```
create make_squares function that receives an array.
    declare list squares

    create a loop for all the values in the array
        obtain the squeared of the current value

        if the squares is empty, just append it
              continue

        check where to insert
        if squeared <= squares[0]:
            insert at 0
            continue

        find its place somewhere in the middle of the array
        # I know the possitions can't be 0 or -1
        create a while from 1 to -2
        while j < len(squares):
            check if there I can add it

            before moving ahead, I will check if the next value>squeared. (I will never check in a non existing value in this case)

            j += 1

    return squares
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(nLogn):** Because I have a while when I need to check where to insert the value in the middle

**Space O(n):** I'm not creating any additional DS.

### CODE

[cracking_practices/squaring_a_sorted_array/squaring_a_sorted_array.py](squaring_a_sorted_array.py)

### TESTS

[tests/test_squaring_a_sorted_array.py](../../tests/test_squaring_a_sorted_array.py)

### GITHUB BRANCH

[Pull Request # 52, Branch: squaring_a_sorted_array](https://github.com/ilealm/cracking-practices/pull/52)
