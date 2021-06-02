[Table of Contents](../../README.md)

# Problem Get middle node of Linked List

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN

Using a linked list, return the middle node value from the end.  Use O(n) for time and space.

### VISUALS

```
[10] -> [20] -> [30] -> [40] -> [50] -> [60] -> [70] -> [80] -> [90] -> [100] -> None
Middle : 50

[10] -> [20] -> [30] -> [40] -> [50] -> None
Middle : 30

[10] -> [20] -> [30] -> [40] -> None
Middle : 20


```

### EDGE CASES

- The linked list can have any length.
- K is a possitive number.
- K can be bigger than len(linked list)
- Linked list can be empty.
- Is a singly linked list.

### ALGORITHMS

#### APPROACH 1,

```
 establish two pointers, current and runner to the head.
 while possible, move:
    runner 2 possitions
    if runner is not None, move current 1 possiotion

 return current.value

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse the linked list only once.

**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/linked_list_get_middle/linked_list_get_middle.py](linked_list_get_middle.py)

### TESTS

[tests/test_linked_list_get_middle.py](../../tests/test_linked_list_get_middle.py)

### GITHUB BRANCH

[Pull Request # n, Branch: linked_list_get_middle](https://github.com/ilealm/cracking-practices/pull/93)
