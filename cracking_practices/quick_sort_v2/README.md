[Table of Contents](../../README.md)

# Problem Quick Sort

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN
This solution implements Quick Sort, but instead of using a helper Partition funtion to sort the less and greater values in the array, this solution implements List Comprenhension istead.

### VISUALS

```
original array
[25, 50, 15, 6, 35, 1, 27]
pivot (array[0]): 25
less: [6, 1, 15]
greater:  [35, 27, 50]


recursion left side: [6, 1, 15]
less : [1, 6]

recursion right side:
less: [27, 35]

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- Values can be letters

### ALGORITHMS

#### APPROACH 1, Implementing Comprenhension Lists to get min and max from pivot

```
Implement a function quicksort receives an array
    stablish base case, if len(array) <2 return the array
    stablish the pivot at index 0
    using list comprenhension, get a array with all the values equal or less than pivot.
    using list comprenhension, get a array with all the values greater than pivot.
    return recursive call on quicksort(array_less) + pivot + quicksort(array_greater)

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(nLogn):** I need to touch all the elements at least once, and more times in the recursion.

**Space O(1):** I'm not creating new DS.

### CODE

[cracking_practices/quick_sort_v2/quick_sort_v2.py](quick_sort_v2.py)

### TESTS

[tests/test_quick_sort_v2.py](../../tests/test_quick_sort_v2.py)

### GITHUB BRANCH

[Pull Request # n, Branch: quick_sort_v2](https://github.com/ilealm/cracking-practices/pull/89)
