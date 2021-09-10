[Table of Contents](../../README.md)

# Problem Priority Queue

<!-- [Whiteboard approach](priority_queue) -->

### PROBLEM DOMAIN
Implement a Priority Queue using an array. The methods should include add and remove.
The remove method should return the greatest value in the array.


### VISUALS

```
F = Front
R = Rear
queue:
[10, 30, 40, 50]

Add : 20
[10, 20, 30, 40, 50]


Remove : return :50
[10, 20, 30, 40 ]

```

### EDGE CASES

- The priority is deterninated by the value to be pushed.
- Values can be repeted.
- I can have empty array.
- In this scenario, the array has a fixed length.
- The right possition of value to add is at front of the queue.
- The right possition of value to add is at end of the queue.
- This will not be a cycling list, BC the remove will take the greatest value (the rightmost).

### ALGORITHMS

#### APPROACH 1, Iterate the array (queue) from the REAR to find the right possition, if the possition is not the right, move the value to the left. For remove, I will return the greatest value in the array (the right most)

```
create class PriorityQueue()

    def __init()
        queue = [] * size
        count = int

    def is_empty()
        return len(queue) == 0

    def is_full()
        return count == size

    def add(value)
        if is_full
            raise exception

        i_to_add = switch_items_to_right(value)

        queue[i_to_add] =  value
        count ++


    def remove()
        if is_empty()
            raise error

        return queue[count--]


    def switch_items_to_right(value)
        if count == 0
            return 0

        current = count // start at the right
        while value < queue[current]
            if value < queue[current]:
                queue[current+1] = queue[current]

            current --

        return current





```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time Add O(n):** In worst case I will need to swap all the values to the right.

**Space Remove O(1):** I'm just retrieving the rightmost element.

### CODE

[cracking_practices/priority_queue/priority_queue.py](priority_queue.py)

### TESTS

[tests/test_priority_queue.py](../../tests/test_priority_queue.py)

### GITHUB BRANCH

[Pull Request # n, Branch: priority_queue](https://github.com/ilealm/cracking-practices/pull/X)
