[Table of Contents](../../README.md)

# Problem Employee Free Time

### PROBLEM DOMAIN
For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.


### VISUALS

```

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- I will assume that each pair or list is a 2 shifts employees's working time in a day, so 4 lists means 2 employees schedules.


### ALGORITHMS

#### APPROACH 1,

```
    # Fill working_hours with true for whenever is someone working on that hour.
    # traverse all the employees (i) and their shifts(j), and then, set working_hours to true for all the hours the employee
    # has assigned job.
    # Also, I will keep track of the bigest hour to latter I can search for all the gaps.
               # Fill the hours of the current shift

    # Find gaps where all the employes are not working, in other words, where working_hours = False

    # check for special cases

    # return value

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(nLogn):** I need to have nested loops to traverse all the input.

**Space O(n):** I'm create new ds depenfing on input.

### CODE

[cracking_practices/employee_free_time/employee_free_time.py](employee_free_time.py)

### TESTS

[tests/test_employee_free_time.py](../../tests/test_employee_free_time.py)

### GITHUB BRANCH

[Pull Request # 76, Branch: employee_free_time](https://github.com/ilealm/cracking-practices/pull/76)
