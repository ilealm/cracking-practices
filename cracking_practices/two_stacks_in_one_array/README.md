[Table of Contents](../../README.md)

# Problem Implement two stacks in one array.

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN
Implement two stacks in one array. Support these operations:

push1() // to push in the first stack

push2() // to push in the second stack

pop1()

pop2()

isEmpty1()

isEmpty2()

isFull1()

isFull2()

Make sure your implementation is space efficient. (hint: do not allocate the same amount of space by dividing the array in half.)


### VISUALS

```
Based on my approach to append to right and left, on one array, and when push1 and pop1 are operations to the left, and push2, and pop2 are operations to the right of the array.
array:[None, None, None, None, None, None, None, None, None, None,  ]


push1(1)
array:[1, None, None, None, None, None, None, None, None, None,  ]


```

### EDGE CASES

- I can Add more items in side 1 than side 2.
- Add all items in side 1 or all in side 2.
- I can add in side 1 or 2 as long I can have space.
- I only can use 1 array for the stack management.

### ALGORITHMS

#### APPROACH 1: Have one array, and push1 and pop1 are operations to the left for the array. Push2 and pop2 are operations to the right of the array. I will use pointers to know the possition where to push/pop on left or right.


```
pop1/push1 : movements on the left side of the array.
pop2/push2 : movements on the right side of the array.

create a class Stack
on __init_ method declare the size of the array, pointers left/righ and the array that will be the stack


<!-- movements to the left end of the array -->
def push1(value):
    if is_stack_full? return

    increase pointer_left by 1
    insert at array[pointer_left]

def pop1(value):
    if pointer_left == 0 raise error

    <!-- I will not reasing a new value to the poped position, is pointless -->
    decrease pointer_left by 1
    return array[pointer_left]


<!-- movements to the right end of the array -->
def push2(value):
    if is_stack_full? return

    decrease pointer_right by 1
    insert at array[pointer_right]

def pop2(value):
    if pointer_right == 0 raise error

    <!-- I will not reasing a new value to the poped position, is pointless -->
    top_value = array[pointer_right+1]
    increase pointer_right by 1
    return top_value


<!-- heleper functions -->
def is_stack_full()
    return pointer_left == pointer_right


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
