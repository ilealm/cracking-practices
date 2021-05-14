[Table of Contents](../../README.md)

# Problem Using Recursion, get the sum of all elements in an array.

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN
- Using Recursion, get the sum of all elements in an array.
- Using Recursion, get the number of elements in an array.
- Using Recursion, find the bigest number of elements in an array.
- Using Recursion and binary search, find a value in a list. If the value is not there, return -1.

### VISUALS

```
array = [1,2,3,4,5]
sum = 15
num_elements = 5
max_element = 5
recursion_binary_search: 5

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1,

```
SUM
create a function recursion_sum that receives one array.
    stablish base case
    if len(array) == 1:
        return(array[0])

    # on each recursion, I will send a 1 space smaller array
    and I will return the sum of the recuersion returned value and the first position in the array
    return array[0] + recursion_sum(array[1:])


NUMBER OF ELEMENTS
create a function that receives an array
    if the array is empty, return 0

    create base case: if len(array) == 1, return 1

    return 1 + recursive function, senfing the array - 1 left position


MAX ELEMENT IN THE LIST
create a function that receives an array
    base case, if len(array) == 1, return array[0]

    return the max of a recursive call and the value of array[0]


BINARY SEARCH

create a function that receives an array and a target
    add base case

    stablish left, right and middle
    check if middle is the target, if so, returns its value

    determinate if I will call recursively the left or right part of the array
    do the recursion

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to

**Space O(n):** I'm

### CODE

[cracking_practices/recursion/recursion.py](recursion.py)

### TESTS

[tests/test_recursion.py](../../tests/test_recursion.py)

### GITHUB BRANCH

[Pull Request # n, Branch: recursion](https://github.com/ilealm/cracking-practices/pull/88)
