[Table of Contents](../../README.md)

# Problem

Implement a Selection Sort in a List.

### PROBLEM DOMAIN

 Given a unsorted list, return the same list in an ordered fashion using Selection Sort. The sorting must be in place.

### VISUALS

```
given:
    array = [ 45, 30, 5, 45, 6, 30, 25]

return:
    expected = [5, 6, 25, 30, 30, 45, 45]

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- Array can be empty.
- Array can contain letters.

### ALGORITHMS

#### APPROACH 1

```

def selection_sort(array):
    # sablish my left pointer
    current_index = 0

    # traverse all the array from current_index+1, to find the min value
        # I need to stablish on each round, the new min value and it's index
        # use a traversing_index variable, which always will start one step ahead of current_index
        traversing_index = current_index + 1
        while traversing_index < len(array):
            # check if where I'm is the new min, if so, set new min values
            # increase the traversing_index
            traversing_index += 1


        # swap the values from my current_index to the new min

        # move to the next index
        current_index += 1
    return array

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n2):** Because I have inner lopps and I'm touching each element on each loop, which creates n*n = n2
**Space O(1):** I'm creating the sorting in place, no no additional space is required.

### CODE

[cracking_practices/selection_sort/selection_sort.py](selection_sort.py)

### TESTS

[tests/test_selection_sort.py](../../tests/test_selection_sort.py)

### GITHUB BRANCH

[Pull Request # n, Branch: selection_sort](https://github.com/ilealm/cracking-practices/pull/86)
