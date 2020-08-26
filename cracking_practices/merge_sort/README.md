[Table of Contents](../../README.md)


# Problem Merge Sort List

[Whiteboard approach](https://docs.google.com/document/d/1tMuwG8EBPvnVffP0HQg_A3xrq0Q7XJEt9uNPJ1qi6S4/edit?usp=sharing)

### PROBLEM DOMAIN
Given a list filled with unsorted numbers, return the list in sorted order using a merge sort algorithm.

### INPUT
[50, 35, 90, 75, 10, 60]

### OUTPUT
[10, 35, 50, 60, 75, 90]



### EDGE CASES
- The algorithm MUST use merge sort.
- The algorithm must be in place.
- The list can be any length.


### ALGORITHMS

```
create a merge_sort function that receives an array
	if the array is empty, return an empty list
set num_elements to len(array)

# set base case to exit the recursion
if num_elements is equal to 1, return

set middle variable to the middle of the array
	set left to array from 0 to middle
set right to array from middle to the end of array

	call merge_sort sending left
	call merge_sort sending right

	call merge_helves and send left, right and array

	return array

create merge_helves function and receive left, right and array
	create pointers from right, left and array, and set to 0

	create a loop while left and right pointers are less than len of they sub arrays
	if right[right_pointer] < left[left_pointer]
move values on the array
		increase right pointer by 1
      else
           move values on the array
           increase left pointer by 1

increase array pointer by 1


   # add the elements that wasn't already added, from the left
   loop while left_pointer is less len(left):
      move values to array
      increase left pointer by 1
increase array pointer by 1

   # add the elements that wasn't already added, from the right
   loop while right_pointer is less len(right):
      move values to array
      increase right pointer by 1
increase array pointer by 1

```


#### TESTS
```
[50, 35, 90, 75, 10, 60]
[50, 35, 90] [75, 10, 60]
[50] [35, 90]
[35] [90]
[35, 50, 90]
		 [75, 10, 60]
		 [75] [10, 60]
		      [10] [60]
		      [10, 60]
		  [10, 60, 75]

[35, 50, 90] [10, 60, 75]
         ^             ^
[10, 35, 50, 60, 75, 90]
                      ^
pointer ^: 0
left ^: 0
right ^: 0
```


#### BIG O
**Time O(nLogn):** Because I traverse all the list, and then traverse logn times again to make the movements.

**Space O(n):** I create a helper ds.

### CODE
[cracking_practices/merge_sort/merge_sort.py](merge_sort.py)


### TESTS
[tests/test_merge_sort.py](../../tests/test_merge_sort.py)

### GITHUB BRANCH

[Pull Request # 18, Branch: merge_sort](https://github.com/ilealm/cracking-practices/pull/18)
