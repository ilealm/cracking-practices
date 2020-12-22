[Table of Contents](../../README.md)

# Problem Intervals Intersection


### PROBLEM DOMAIN
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.


### VISUALS

```
Example 1:
Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]

Example 2:
Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- The lists are sorted.

### ALGORITHMS

#### APPROACH 1, finding overlaps

```
    # traverse b to find intersecctions on a
        # check if not fit at all

        # check if b fits in a

        # check if b have interseccion with a, but b is bigger
            # add the rest of the interseccion

    return result
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(nm):** I need to traverse both inputs.

**Space O(n):** I'm in worst case scenario when both lists overlaps.

### CODE

[cracking_practices/intervals_intersection/intervals_intersection.py](intervals_intersection.py)

### TESTS

[tests/test_intervals_intersection.py](../../tests/test_intervals_intersection.py)

### GITHUB BRANCH

[Pull Request # 72, Branch: intervals_intersection](https://github.com/ilealm/cracking-practices/pull/72)
