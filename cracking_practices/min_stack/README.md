[Table of Contents](../../README.md)

# Problem: MinStack

### PROBLEM DOMAIN

Design a stack that supports push, pop and retrieving the minimum value in constant time.


### VISUALS
```
For example, we populate our stack with [5, 2, 10, 1] (from left to right).

        1  <-- top
        10
        2
        5

stack.min() // 1
stack.pop()
stack.min() // 2

```

### EDGE CASES

- I can have diplicated values.
- Values will be numeric.
- Values can be negative.
- Values does not have an order.


### ALGORITHMS

#### APPROACH 1: Have 2 stacks: one for all the values and one for all the min values. After a push, if the pushed value is less than the the top of min_stacks, add the value also there. On a pop, is the poped value is the same as the top of min_stack, also poped from there.

```
import colllections.deque
create a class Stack() with this methods
    on __init__:
        stack = deque()
        min_stack = deque()

    create method top()
        if len(stack) == 0 : return None
        return stack[-1]

    create method min_top()
        if len(min_stack) == 0 : return None
        return min_stack[-1]

    create method push(value)
        push value to stack
        if not min_top is None and
            value < min_top :
                push vaue in min_top


    create method pop()
        if len(stack) == 0 : return None

        if top() ==  min_top():
            min_pop()

        return stack.deque()

    create method min_pop()
        if len(stack) == 0 : return None

        min_stack.deque()

    create method min():
        if len(stack) == 0 : return None
        return min_stack[1]

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to use a two stacks that can flexibly grow.

**Space O(1):** I'm retrieving the min value in constant time.

### CODE

[cracking_practices/min_stack/min_stack.py](min_stack.py)

### TESTS

[tests/test_min_stack.py](../../tests/test_min_stack.py)

### GITHUB BRANCH

[Pull Request # n, Branch: min_stack](https://github.com/ilealm/cracking-practices/pull/96)
