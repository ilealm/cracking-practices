[Table of Contents](../../README.md)


# Problem Average Subarrays

<!-- [Whiteboard approach](X) -->

### PROBLEM DOMAIN
Problem Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

### VISUALS
input: Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

Output: [2.2, 2.8, 2.4, 3.6, 2.8]


### EDGE CASES
- The array can be empty.
- K can be bigger than the array.
- Aim for O(n)
- The array will contain only integers.


### ALGORITHMS

# APPROACH 1, Sliding Window: I will get the sum of the values of a current "window" whit the values of the substring k;
# then, before moving to the next window, I will delete from sum the left pointer, add 1 to both pointers
# then add to sum the new value at the right
#### APPROACH 1,

```
declare funcion average_subarrays than receives an array and K
    add basic validations

    declare and set variales:
    arr_result
    left_pointer = 0
    right_pointer = K - 1
    sum = 0

    get the first sum of the current window inside the array

    loop to the rest of the array until I have a window to move,
    moving one position to right, then substracting position left, and sum new position right

        append sum to arr_result

        substract the value of left, and then I move the pointers


        # move pointers
        left_pointer += 1
        right_pointer += 1 (validate I'm not out of index)

        add the new "window value" to the sum. Now I will have all the values of the current "window"


    return arr_result
```


#### TESTS
```
array = [10,20,30,40,50]
K = 2

left_pointer = 0,1,2,3
right_pointer = 1,2,3,4
arr_return: [15, 25, 35, 45]

```


#### BIG O
**Time O(n):** I', only traversing once the array.

**Space O(n):** I'm creating one array that can have different lengt.

### CODE
[cracking_practices/average_subarrays/average_subarrays.py](average_subarrays.py)


### TESTS
[tests/test_average_subarrays.py](../../tests/test_average_subarrays.py)

### GITHUB BRANCH

[Pull Request # 35, Branch: sliding_window](https://github.com/ilealm/cracking-practices/pull/35)
