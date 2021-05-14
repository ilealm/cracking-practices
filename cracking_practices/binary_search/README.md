[Table of Contents](../../README.md)

# Problem



### PROBLEM DOMAIN

Implement a Binary search to find a value in a list. If the value exists, return the value's index, otherwise, return -1.


### VISUALS

```
array = [5, 10, 15, 20, 25, 30, 35, 40]
indices  0,  1,  2,  3,  4,  5,  6,  7
value_to_find = 35
value to return = 5



```

### EDGE CASES

- The list will be sorted.
- Values can't be repeted.
- The list can have numbers or letters.
- The list can be empty.

### ALGORITHMS

#### APPROACH 1,

```
create a function that receives an array and a value_to_find.

    #stablish my left and right pointers
    left = 0
    right = len(array) - 1

    # create a loop
    while left <= right:
        # get the middle of my array
        # compare if middle is the value I'm looking for, if is, return it
        if array[middle] == value_to_find:
            return middle
        # if not, check if I need to move to left or right and move pointers
        if value_to_find < array[middle]:
            right = middle - 1
        else:
            left = middle + 1

    # If I get to here means I didn't found the value, so return -1
    return -1

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(logn):** I need to traverse everytime the half of the array.
**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/binary_search/binary_search.py](binary_search.py)

### TESTS

[tests/test_binary_search.py](../../tests/test_binary_search.py)

### GITHUB BRANCH

[Pull Request # n, Branch: binary_search](https://github.com/ilealm/cracking-practices/pull/X)
