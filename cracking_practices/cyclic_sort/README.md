[Table of Contents](../../README.md)

# Problem Cyclic Sort

[ ](cracking_practices/cyclic_sort/README.md)
- We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

### PROBLEM DOMAIN

### VISUALS

```

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1,

```
    set a pointer_left to 0
    traverse all the array while pointer_left < len(array)
        get the swap_pointer is the place where pointer_left will swap
        swap_pointer = nums[pointer_left] - 1
         ckeck if the value of pointer_left is in the right place, in this case, when both are pointing to the same spot.
         if pointer_left == swap_pointer:
            increase pointer_left by 1
        else:
            swap the values of pointer_left with the value of swap_pointer
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the array.

**Space O(1):** I'm not creating new space.

### CODE

[cracking_practices/cyclic_sort/cyclic_sort.py](cyclic_sort.py)

### TESTS

[tests/test_cyclic_sort.py](../../tests/test_cyclic_sort.py)

### GITHUB BRANCH

[Pull Request # 76, Branch: cyclic_sort](https://github.com/ilealm/cracking-practices/pull/76)
