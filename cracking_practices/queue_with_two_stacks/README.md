[Table of Contents](../../README.md)

# Problem Queue With Two Stacks

### PROBLEM DOMAIN
Implement a queue using two stacks.


### VISUALS

```
F = Front
R = Rear
        F       R
queue: [10, 20, 30]

```

### EDGE CASES

- I can have any values in the arays.
- Values can be repeted.
- The queue can be any size.

### ALGORITHMS

#### APPROACH 1, Enqueue values to stack1, on dequeue, if stack2 is empty, fill it with the reversed stack1, then pop from stack2; if stack2 is not empty, just pop from there

```

import collections.deque

create a class Queue
    create def __init:
        stack_push = deque()
        stack_pop = deque()


    create def push(value):
        stack_push.push(value)


    create def dequeue():
        if is_empty():
            Exeption("The queue is empty)


        if stack_pop_is_empty()
            fill_stack_pop()

        return stack_pop.pop()

    <!-- checks that both stacks are empty -->
    create is_empty()
        return (len(stack_push) == 0) and (len(stack_pop) == 0)

    create stack_pop_is_empty()
        return (len(stack_pop) == 0)

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Enqueue O(1):** I just need to add at the end of the queue.

**Dequeue O(n):** In worst case scenario I need to reverse all the queue.

### CODE

[cracking_practices/queue_with_two_stacks/queue_with_two_stacks.py](queue_with_two_stacks.py)

### TESTS

[tests/test_queue_with_two_stacks.py](../../tests/test_queue_with_two_stacks.py)

### GITHUB BRANCH

[Pull Request # n, Branch: queue_with_two_stacks](https://github.com/ilealm/cracking-practices/pull/X)
