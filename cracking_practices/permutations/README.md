[Table of Contents](../../README.md)


# Problem Permutations

[Whiteboard approach](https://docs.google.com/document/d/1UfeY35aJqW-NJbIfpLOwV9UXQgRzNlv3wm9eCNBg-3Q/edit?usp=sharing)

### PROBLEM DOMAIN
Given an array, return all the possibles permutations of it.

### INPUT

array = [1, 2, 3]


### OUTPUT

expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


### EDGE CASES
- The array can be n length.
- The array can have duplicates.
- Each permutation should be unique.


### ALGORITHMS

```
create a function which will be recursive, and will receive an array, a permutation array, and a perms array


   # exit case:
   if array is empty, the permutation in permutation array, so append it to perms

   create a loop for each element in the array
       call recursive permutation, sending the original array minus the current element, permutations array, and perms array
       remove the last element of permutation, so I can a clean array for the next recursive

   return perms

```


#### BIG O
**Time O(n!):** I need to create all possible combinations, which is a factorial of the list.

**Space O(1):** I don't create new ds.

### CODE
[cracking_practices/permutations/permutations.py](permutations.py)


### TESTS
[tests/test_permutations.py](../../tests/test_permutations.py)

### GITHUB BRANCH

[Pull Request # 30, Branch: permutations](https://github.com/ilealm/cracking-practices/pull/30)
