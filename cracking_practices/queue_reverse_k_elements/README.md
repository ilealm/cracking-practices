[Table of Contents](../../README.md)

# ProblemQueue reverse k elements

### PROBLEM DOMAIN
Given an integer K and a queue of integers, write code to reverse the order of the first K elements of the queue.

### VISUALS

```

Input:  Q = [10, 20, 30, 40, 50]

K = 3O

0utput: Q = [30, 20, 10, 40, 50]

```

### EDGE CASES

- I can have an empty queue.
- K can be any integer.

### ALGORITHMS

#### APPROACH 1, From the queue, pass k elements to a stack, and the rest of the queue to a temporarly queue. Then create a new queue with the poped values of the stack and then the values of the queue.

```
create a class queue
    ...
create a class stack
    ...

create method queue.reverse_k(k)
    if k > len(queue):
        raise Exception

    s = stack()
    for i to k, i++:
        s.add(q.pop())

    // save the rest of the queue in a temporaly queue
    temp_q = queue()
    while not  q_is_empty():
        temp_p.add(q.pop())

    // merge the stack and queue
    while not s_is_empty()
        q.add(s.pop())

    while not temp_q_is_empty()
        q.add(temp_q.pop())

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the stack.

**Space O(1):** I'm no creating data copies, just realocating on the memory.

### CODE

[cracking_practices/queue_reverse_k_elements/queue_reverse_k_elements.py](queue_reverse_k_elements.py)

### TESTS

[tests/test_queue_reverse_k_elements.py](../../tests/test_queue_reverse_k_elements.py)

### GITHUB BRANCH

[Pull Request # n, Branch: queue_reverse_k_elements](https://github.com/ilealm/cracking-practices/pull/101)
