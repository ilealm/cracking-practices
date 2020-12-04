[Table of Contents](../../README.md)

# Problem Minimum Window Sort
<!-- [Whiteboard approach](minimum_window_sort) -->

### PROBLEM DOMAIN
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

### VISUALS
```
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

#### APPROACH 1, Sliding windows

```
    traverse all the array, and on each possition I will peek the next one.
    if next < current, I will create a window from current until I find a bigger number than current
    I will have a window_min, and check against previous_current, if window_min < previous_current, I will
    grow my window 1 space to left.
    save min


    while current < len(arr)-1 and current >= 0: # is -1 BC I use a peek

        check if the next is < current
        if arr[current] > arr[current+1]:
            I will create a window from current to a bigger number than current

            from this point I know is unsorted, so I need to find the maximous value in all the array
            so later I can stabish the window

            if I didn't found a bigger value means the array is sorted in reverse.

            obtain the smallest

            since I found a window, I will check the rest of the values BUT
            from my current window, so I will move current to right

        else:
            move my current to the next position


    return smallest
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse the array only once.

**Space O(1):** I'm not creating new DS based on N.

### CODE

[cracking_practices/minimum_window_sort/minimum_window_sort.py](minimum_window_sort.py)

### TESTS

[tests/test_minimum_window_sort.py](../../tests/test_minimum_window_sort.py)

### GITHUB BRANCH

[Pull Request # 60, Branch: minimum_window_sort](https://github.com/ilealm/cracking-practices/pull/60)
