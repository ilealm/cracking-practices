[Table of Contents](../../README.md)

# Problem Classroom Scheduling

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN

You have a classroom and a schedule, and want to hold as many classes there as possible.
Some clases may overlap, so you need to arrainge the classes in the most optimal way

### VISUALS

```
classes = [
        ["07:00", "08:00"],
        ["09:00", "10:00"],
        ["09:30", "10:30"],
        ["10:00","11:00"],
        ["10:30:","11:30"],
        ["11:00","12:00"]]

Schedule without overlaping

[['07:00', '08:00'], ['09:00', '10:00'], ['10:00', '11:00'], ['11:00', '12:00']]


```

### EDGE CASES

- I will have hour and minute times on each slot of the array.
- The first value in the array is the class start and the second is the class end hour.
- Values are not repeted.
- Hours are in 24 hour format.
- Array is unsorted.

### ALGORITHMS

#### APPROACH 1,

```

Create a function that receives an array of hours
    declare some helper variables: end_hour = 23
    create a loop to search in all the array:
        find the class that ends earlier (calling a helper function)
        set the ending hour of this class, as the start point for the next class.
        find the class that starts after or at this time
        if founded
            set as my new ending hour
            append to schedule array
        return schedule

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n2):** In this case, the array is not sorted and I need to traverse twice to find all the spots. Probably, if I sort the array at the beggining I don't need to traverse it twice.

**Space O(n):** I'm returning an array (schedule) which can be the same length of the input array.

### CODE

[cracking_practices/class_scheduling/class_scheduling.py](class_scheduling.py)

### TESTS

[tests/test_class_scheduling.py](../../tests/test_class_scheduling.py)

### GITHUB BRANCH

[Pull Request # n, Branch: class_scheduling](https://github.com/ilealm/cracking-practices/pull/X)
