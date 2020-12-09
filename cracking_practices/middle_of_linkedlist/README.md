[Table of Contents](../../README.md)

# Problem Middle of the LinkedList

### PROBLEM DOMAIN
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
If the total number of nodes in the LinkedList is even, return the second middle node.

### VISUALS

```
Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Example 2:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4

Example 3:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- Is a Singly LL

### ALGORITHMS

#### APPROACH 1, 2 pointers: slower and faster. Faster will move 2x and will be the one I will be moving

```
declare a function that receives a LL head
    set to pointes, slower and faster to head
    create a while faster and faster.next
        move 1 slower, 2x faster

    return slower.value
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the LL only once.

**Space O(1):** I'm not creating any new DS.

### CODE

[cracking_practices/middle_of_linkedlist/middle_of_linkedlist.py](middle_of_linkedlist.py)

### TESTS

[tests/test_middle_of_linkedlist.py](../../tests/test_middle_of_linkedlist.py)

### GITHUB BRANCH

[Pull Request # 66, Branch: middle_of_linkedlist](https://github.com/ilealm/cracking-practices/pull/67)
