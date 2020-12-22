[Table of Contents](../../README.md)

# Problem

<!-- [Whiteboard approach](insert_interval) -->

### PROBLEM DOMAIN

### VISUALS

```

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, Finding intervals

```
def insert(intervals, new_interval):
    merged = []

    ni_start = new_interval[0]
    ni_end = new_interval[1]

    new_start = new_end = 0
    new_interval_appended = False

    for i in range(0,len(intervals)):

        # if I already appended the new interval, just append the rest of the intervals
        if new_interval_appended:
            merged.append(intervals[i])
            continue

        if ni_start > intervals[i][1]:
            # there is no overlap with interval
            merged.append(intervals[i])
            continue

        # check for overlap when the new interval is smaller than current start
        if ni_start < intervals[i][0]:
            # there is a overlaping. Obtain the new end and start
            new_start = min(ni_start, intervals[i][0])
            new_end = max(ni_end, intervals[i][1])

            # BS is an ordeded array, I need to check if the next position overlaps the current I'm goin to append
            if i < len(intervals):
                if intervals[i+1][0] <= new_end:
                    new_end = intervals[i+1][1]
                    merged.append([new_start, new_end])

                    break

            new_interval_appended = True
            merged.append([new_start, new_end])


    return merged

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the input.

**Space O(n):** Worst case scenario I will have a copy of N.

### CODE

[cracking_practices/insert_interval/insert_interval.py](insert_interval.py)

### TESTS

[tests/test_insert_interval.py](../../tests/test_insert_interval.py)

### GITHUB BRANCH

[Pull Request # 71, Branch: insert_interval](https://github.com/ilealm/cracking-practices/pull/71)
