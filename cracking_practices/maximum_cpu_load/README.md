[Table of Contents](../../README.md)

# Problem Maximum CPU Load
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

### PROBLEM DOMAIN

### VISUALS

```
Example 1:
Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the
jobs are running at the same time i.e., during the time interval (2,4).


Example 2:
Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.

Example 3:
Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].
```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.
- Array are not sorted

### ALGORITHMS

#### APPROACH 1

```
    sort the jobs

    declare valiables to store maximus

    create a loop to traverse all the jobs

        check if the next jobs are overlaping
                If I have an overlaping, so I will use a flag to know which value returns
                sum the cpu loads
            else:
                break the loop

        obtain max values

    return values.
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(nLogn):** I need to sort the array, and then search for colitions.

**Space O(n):** I'm not creating new ds.

### CODE

[cracking_practices/maximum_cpu_load/maximum_cpu_load.py](maximum_cpu_load.py)

### TESTS

[tests/test_maximum_cpu_load.py](../../tests/test_maximum_cpu_load.py)

### GITHUB BRANCH

[Pull Request # 74, Branch: maximum_cpu_load](https://github.com/ilealm/cracking-practices/pull/74)
