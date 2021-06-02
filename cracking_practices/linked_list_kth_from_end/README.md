[Table of Contents](../../README.md)

# Problem kth Element from a Linked List

<!-- [Whiteboard approach](linked_list_kth_from_end) -->

### PROBLEM DOMAIN
Using a linked list, return the kth node value from the end.  Use O(n) for time and space.

### VISUALS

```
[10] -> [20] -> [30] -> [40] -> [50] -> [60] -> [70] -> [80] -> [90] -> [100] -> None
k = 3
kth_from_end = 70

k = 1
kth_from_end = 90

k = 15
kth_from_end = "K is bigger than the linked list"

k = 0
kth_from_end = "100"

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
create a function inside class LinkedList that accepts k
    validate that k > 0
    create variable current and runner and set to head
    create runner gap of k "jumps"
    create traversing one jump at a time for runner and current together while runner has not reaching the end.
    return current.value

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse the LinkdedList only once.

**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/linked_list_kth_from_end/linked_list_kth_from_end.py](linked_list_kth_from_end.py)

### TESTS

[tests/test_linked_list_kth_from_end.py](../../tests/test_linked_list_kth_from_end.py)

### GITHUB BRANCH

[Pull Request # n, Branch: linked_list_kth_from_end](https://github.com/ilealm/cracking-practices/pull/92)
