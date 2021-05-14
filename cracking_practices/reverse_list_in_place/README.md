[Table of Contents](../../README.md)

# Problem Reverse a List in Place


### PROBLEM DOMAIN
Create a function that receives a list and return the same list but with the elements in inverted order.

### VISUALS

```
array=['a', 'b', 'c', 'd', 'e']

expected =['e', 'd', 'c', 'b', 'a']

array=[1,2,3,4,5,6,7,8,9,10]

expected =[10,9,8,7,6,5,4,3,2,1]

```

### EDGE CASES

- I can have any values in the array.
- Values can be repeted.
- The list can be empty.
- The list can have any length.

### ALGORITHMS

#### APPROACH 1,

```
create a  function reverse_list_in_place that receives one array.
    if len(array) <= 1 return the array
    declare left and right pointer

    create a loop while left<right and swap pointers
        move left and right pointers 1 position closer

    return array

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(Logn):** I need to traverse the half of the list.

**Space O(1):** I'm not creating a new DS.

### CODE

[cracking_practices/reverse_list_in_place/reverse_list_in_place.py](reverse_list_in_place.py)

### TESTS

[tests/test_reverse_list_in_place.py](../../tests/test_reverse_list_in_place.py)

### GITHUB BRANCH

[Pull Request # n, Branch: reverse_list_in_place](https://github.com/ilealm/cracking-practices/pull/87)
