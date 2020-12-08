[Table of Contents](../../README.md)

# Problem Length of the Cycle in LL
Given the head of a LinkedList with a cycle, find the length of the cycle.



### PROBLEM DOMAIN

### VISUALS

```
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle length: " + str(find_cycle_length(head)))  --> 4

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle length: " + str(find_cycle_length(head)))  --> 3

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- Can or nor have cycle.

### ALGORITHMS

#### APPROACH 1, Having a slower and faster(2x) pointers

```
    set:
    slower = head
    faster = head.next.next
    counter = 0
    start_counting = False

    while faster and faster.next:
        check if I founded the loop, if so I will start counting:
            I'm going to start counting, so reset the position of faster to 2x from slower (this will be my start point)
        else:
            I finished counting the second loop, so return the count and exit the cycle
            return counter

        check if start_counting flag is true, if so, add 1 to counter

        move pointers as usual

    return counter

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the array.

**Space O(1):** I'm not creating new ds depending on input.

### CODE

[cracking_practices/linked_list_cycle_length/linked_list_cycle_length.py](linked_list_cycle_length.py)

### TESTS

[tests/test_linked_list_cycle_length.py](../../tests/test_linked_list_cycle_length.py)

### GITHUB BRANCH

[Pull Request # 62, Branch: linked_list_cycle_length](https://github.com/ilealm/cracking-practices/pull/62)
