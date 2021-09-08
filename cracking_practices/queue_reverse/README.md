[Table of Contents](../../README.md)

# Problem Reverse a Queue

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN
Reverse a Queue.

### VISUALS

```
Original queue
top              back
[10, 20, 30, 40, 50]

Reversed queue
top              back
[50, 40, 30, 20, 10]

```

### EDGE CASES

- Doesn't have to be in place

### ALGORITHMS

#### APPROACH 1, Use an auxiliary stack to save the values, then fill the queue again with the stack's values.

```
import collections.deque

create class Stack
    create __Init__
        self.stack = deque()

    create method push(value)
    create method pop()
    create method top()
    create method is_empty()


create class Queue()
    create __Init__
        self.queue = deque()


    create method push(value)
        self.queue.push(value)

    create method pop()
        if not_empty:
            self.queue.popleft()


    create method is_empty()
        return len(queue) == 0

    create method reverse():
        stack = Stack()
        if is_empty: return

        <!-- save the queue in a a stack -->
        while not self.is_empty():
            stack.push(self.queue.pop())


        <!-- pass the stack to a queue -->
        while not stack.is_empty:
            self.queue.push(stack.pop())

        create method peek()
            if not_empty:
                return self.queue[0]


```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to

**Space O(n):** I'm

### CODE

[cracking_practices/x_x/x_x.py](x_x.py)

### TESTS

[tests/test_x_x.py](../../tests/test_x_x.py)

### GITHUB BRANCH

[Pull Request # n, Branch: x_x](https://github.com/ilealm/cracking-practices/pull/X)
