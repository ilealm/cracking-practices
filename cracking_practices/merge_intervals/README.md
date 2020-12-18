[Table of Contents](../../README.md)

# Problem Merge Intervals

### PROBLEM DOMAIN
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

### VISUALS

```
Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]

Example 2:
Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]

Example 3:
Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- The first value always will be less than the second value.
- On each interval array I only will have 2 values, the 1st representing the beggining and the second representing the end.

### ALGORITHMS

#### APPROACH 1, Merge Intervals

```
create a loop that receives an interval objects array

    create a loop for all the len of interval
        I will compare my current interval to what I already have in merged

        create another loop for the merged

            # Scenario 1: there is no overlaping, if not, I will just add to the merge array.

            # Scenario 2: the current array has a end bigger than something already stored in merge array, if so, it will be
            # join to merge. The start and end of merge could change.

                # I need to stablish the end and start of the new merge
                set flag inteval_overpaled = True

        # if there is not inteval_overpaled, then I add the interval to the merged array
        if not inteval_overpaled:
            merged.append(intervals[i])


    return merged arrays

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n^2):** I need to traverse both arrays to find overlapings.

**Space O(n):** I'm creating a new array to return, in worst case scenario is same as N.

### CODE

[cracking_practices/merge_intervals/merge_intervals.py](merge_intervals.py)

### TESTS

[tests/test_merge_intervals.py](../../tests/test_merge_intervals.py)

### GITHUB BRANCH

[Pull Request # 70, Branch: merge_intervals](https://github.com/ilealm/cracking-practices/pull/70)
