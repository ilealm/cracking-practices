[Table of Contents](../../README.md)


# Problem Implement Quick Sort in List

[Logic from medium.com/basecs](https://medium.com/basecs/pivoting-to-understand-quicksort-part-2-30161aefe1d3)

### PROBLEM DOMAIN
Implement a Quick Sort for a list.

### INPUT, Example
 [10, 15, -3, 12, 1, 30, 7]

### OUTPUT
[-3, 1, 7, 10, 12, 15, 30]



### EDGE CASES
- List already sortered.
- Order in increase fashion.


### ALGORITHMS

#### APPROACH 1, Setting the pivot in the middle
[Logic from](https://medium.com/basecs/pivoting-to-understand-quicksort-part-2-30161aefe1d3)

[Logic from](https://www.youtube.com/watch?v=SLauY6PpjW4&t=474s)


#### BIG O
**Time O(nLogn):** I traverse all the list, then I traverse again in helves.

**Space O(1):** I only use variables and not a copy of the list.

### CODE
[cracking_practices/quick_sort/quick_sort.py](quick_sort.py)


### TESTS
[tests/test_quick_sort.py](../../tests/test_quick_sort.py)

### GITHUB BRANCH

[Pull Request # quick_sort, Branch: 19](https://github.com/ilealm/cracking-practices/pull/19)
