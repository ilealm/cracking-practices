[Table of Contents](../../README.md)

# Problem: Reverse a Linkedlist

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN
Having a linked list, reverse it using O(n) in time and O(1) in space.

### VISUALS

```
# Original LinkedList
#  Head => [10] -> [20] -> [30] -> [40] ->  None

# Reversed
#  Head => [40] -> [30] -> [20] -> [10] ->  None

```

### EDGE CASES

- The Linked list can have N lenght.
- Values can be repeted.
- The Linked list is a sinlgly.
- Values can be anything.
- The linked list can be empty.
- The linked list have only the head attribute.

### ALGORITHMS

#### APPROACH 1,

```
    stablish pointers to previous and current nodes.

    traverse all the LL
        save the next link from the current node
        change the link of current to the previous node (this is the reversing)
        set the previous node as my current possition (for the next round)
        stablish my new possition


    set the head to the last current

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the linked list once.

**Space O(1):** I'm not creating a copy of the linked list, and just need the same variables for creating the reverse.

### CODE

[cracking_practices/linked_list_reverse/linked_list_reverse.py](linked_list_reverse.py)

### TESTS

[tests/test_linked_list_reverse.py](../../tests/test_linked_list_reverse.py)

### GITHUB BRANCH

[Pull Request # n, Branch: linked_list_reverse](https://github.com/ilealm/cracking-practices/pull/91)
