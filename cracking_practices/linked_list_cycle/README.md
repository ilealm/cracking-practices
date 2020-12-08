[Table of Contents](../../README.md)

# Problem LinkedList Cycle


### PROBLEM DOMAIN
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

### VISUALS

```
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))  --> False

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))  --> True

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))  --> True



```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, Slower and Faster by 2 pos.

```
declare a function that receives an LL
    stablish :
    slower to head
    faster to 2  positions ahead of head

    create a while faster
        check if faster == slower, if so, there is the cycle:
            return true

        move pointers:
        slower = slower.next
        faster = faster.next.next


    If I got to this point, I did't find an cycle
    return False

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the LL.

**Space O(1):** I'm not creating new DS depending on the input.

### CODE

[cracking_practices/linked_list_cycle/linked_list_cycle.py](linked_list_cycle.py)

### TESTS

[tests/test_linked_list_cycle.py](../../tests/test_linked_list_cycle.py)

### GITHUB BRANCH

[Pull Request # 61, Branch: linked_list_cycle](https://github.com/ilealm/cracking-practices/pull/61)
