[Table of Contents](../../README.md)

# Problem ArrayQueue AKA Implement a Queue using an array

### PROBLEM DOMAIN
Implement a Queue using an array. It should have this methods push, pop, peek and is_empty.

### VISUALS

```
F = front
R = rear

 F        R
[10, 20, 30, 0, 0]

pop: I got 10, and front chages
    F   R
[0, 20, 30, 0, 0]


push: handle when R at the end of the array, but I have avaiblabe space at the begining of the array.

I want to push 60, and I have space at the beginig of the array
        F      R
[0, 0, 30, 40, 50]

result:
 R      F
[60, 0, 30, 40, 50]

```

### EDGE CASES

- The array will have a fixed position.
- I should not use any extra space.
- Manage pointers to use available spaces once the back or front has reached the end of the array.
- If the array is full, I can't add any more items.

### ALGORITHMS

#### APPROACH 1, Have 2 pointers: front and rear, on each push/pop they will change, also have a items counter and implement circular array manage.

```
create a Queue() class

    def init:
        size = 5  // is the array's size
        queue= [None]* size
        front = 0
        rear =0
        items = 0

    def push(value):
        if is_full():
            error (Array full)

        rear = (rear+1) % size
        queue[rear] = value
        items ++


    def pop():
        if is_empty:
            error (array empty)

        value = queue[front]
        // I could set the value to None just to have a visual idea that is null, but in performance is not a good idea

        front = (front + 1) % size


    def is_full()
        return items == size


    def is_empty()
        return items == 0

    def peek()
        if is_empty():
            error(is empty)

        return queue[front]


```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(1):** I don't need to traverse the structure.

**Space O(1):** I'm just creating one fixed array.

### CODE

[cracking_practices/array_queue/array_queue.py](array_queue.py)

### TESTS

[tests/test_array_queue.py](../../tests/test_array_queue.py)

### GITHUB BRANCH

[Pull Request # n, Branch: array_queue](https://github.com/ilealm/cracking-practices/pull/98)
