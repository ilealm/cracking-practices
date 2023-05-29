[Table of Contents](../../README.md)

# Problem

* Implement Bubble Sort.

### PROBLEM DOMAIN

### VISUALS

```
** Bubble Sort

Input : [8, 2, 4 , 1 , 3]
Output : [1, 2, 3, 4, 8]




```

### EDGE CASES

- Empty array.
- Values can be repeted.
- Possitive values.
- Only two elements in the array.

### ALGORITHMS

#### Bubble Sort

```
Traverse all the array
    on each possition(left), compare it with pointer + 1 (Right)
        if left > right:
            swap them
        increase pointer
        keep traversing until len - interrations

```

#### TESTS

```
Please review the test section below.
```

#### BIG O Buble Sort

**Time O(n2):** I need to iteract multiple times to order all the values.

**Space O(1):** I'm not creating new memory space.

### CODE

[cracking_practices/sorts/sorts.py](sorts.py)

### TESTS

[tests/test_sorts.py](../../tests/test_sorts.py)

### GITHUB BRANCH

[Pull Request # 112, Branch: sorts](https://github.com/ilealm/cracking-practices/pull/112)
