[Table of Contents](../../README.md)

# Problem Conflicting Appointments


### PROBLEM DOMAIN
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

### VISUALS

```
Example 1:
Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Example 2:
Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:
Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- The array will not be sorted.

### ALGORITHMS

#### APPROACH 1, Comparing the end of each interval will the start of the next to search for conflicts.

```
create function can_attend_all_appointments  that receives a list with intervals
    add basic list validations

    Sort the intervals. This way works fine
    Create a loop to check until len-1, if i[end] > i+1[start], if so, return False

    if I made it to this point, means I don't have any overlapping appointments, return True

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(nLogn):** I need to sort the list, and then traverse all list.

**Space O(1):** BC sort is in place.

### CODE

[cracking_practices/conflicting_appointments/conflicting_appointments.py](conflicting_appointments.py)

### TESTS

[tests/test_conflicting_appointments.py](../../tests/test_conflicting_appointments.py)

### GITHUB BRANCH

[Pull Request # 73, Branch: conflicting_appointments](https://github.com/ilealm/cracking-practices/pull/73)
