[Table of Contents](../../README.md)

# Problem Start of LinkedList Cycle

### PROBLEM DOMAIN
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

### VISUALS

```
H = Head
CS = Cycle start

CS: 3
   H               CS
   1  -->  2  -->  3  -->  4  -->  5  -->  6
                   ^-----------------------|


CS: 4
   H                       CS
   1  -->  2  -->  3  -->  4  -->  5  -->  6
                           ^---------------|


CS: 1
   H
   CS
   1  -->  2  -->  3  -->  4  -->  5  -->  6
   ^---------------------------------------|

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- I can assume all my LL are cycled LL.

### ALGORITHMS

#### APPROACH 1, 2 pointers: one slow and other fast

```
    set slower and faster = head

    first, I need to get the length of the cycle, and store it in k variable

    I will move faster k positions ahead

    now, I will move both pointers 1 position until both are at the same place,
    there is the start of the cycle
    
    return slower.value
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse the linked list witout internal lopps.

**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/linked_list_cycle_length/linked_list_cycle_length.py](linked_list_cycle_length.py)

### TESTS

[tests/test_linked_list_cycle_length.py](../../tests/test_linked_list_cycle_length.py)

### GITHUB BRANCH

[Pull Request # 62, Branch: linked_list_cycle_length](https://github.com/ilealm/cracking-practices/pull/62)
