[Table of Contents](../../README.md)

# Problem Linked List Queue


### PROBLEM DOMAIN
- Build a queue using a linked list from scratch. Implement the following operations: enqueue, dequeue, peek, size and is_empty.

### VISUALS

```


LinkedListQueue
R = rear
F = front

enqueue: 10
R  F
[10]

enqueue: 20
R          F
[20] - > [10]

enqueue: 30
R                   F
[30] - > [20] - > [10]

peek() => 10


dequeue =>10 30
R          F
[30] - > [20]



```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, Create a doble LL, mantain front, rear and size as property of the class.

```
create node class
    __init(value)
        value = value
        next=None

create Queue() class
    __init()
        front = None
        rear = None
        size = 0

    def size():
        return size

    def is_empty()
        return size == 0


    enqueue(value)
        create new_node(value)

        if is_empty:
            front = new_node
        else
            new_node.next = rear

        rear = new_node

        size ++

    dequeue():
        if is_empty
            raise error

        r = rear.value

        rear = rear.next
        size --

        if is_empty
            rear = front = None

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time Insert O(1):** I add at the rear of the queue, where I have saved the pointer.
**Time Delete O(1):** I add at the front of the queue, where I have saved the pointer.


### CODE

[cracking_practices/linked_list_queue/linked_list_queue.py](linked_list_queue.py)

### TESTS

[tests/test_linked_list_queue.py](../../tests/test_linked_list_queue.py)

### GITHUB BRANCH

[Pull Request # n, Branch: linked_list_queue](https://github.com/ilealm/cracking-practices/pull/102)
