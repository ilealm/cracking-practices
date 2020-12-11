[Table of Contents](../../README.md)

# Problem Rearrange a LinkedList

<!-- [Whiteboard approach](rearrange_linkedlist) -->

### PROBLEM DOMAIN
Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half
of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has
nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

### VISUALS

```
Example 1:
Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

Example 2:
Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1,

```
My approach for this problem will the tackle in 3 parts:
    1. find the middle,
    2. reverse in place the second half of the LL,
    3. make the zip o both halfs in place

Please view the code section.
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the LL.

**Space O(1):** I'm not creating new DS based on input.

### CODE

[cracking_practices/rearrange_linkedlist/rearrange_linkedlist.py](rearrange_linkedlist.py)

### TESTS

[tests/test_rearrange_linkedlist.py](../../tests/test_rearrange_linkedlist.py)

### GITHUB BRANCH

[Pull Request # n, Branch: rearrange_linkedlist](https://github.com/ilealm/cracking-practices/pull/X)
