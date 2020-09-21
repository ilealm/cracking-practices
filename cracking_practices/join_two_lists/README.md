[Table of Contents](../../README.md)


# Problem Join Two Lists

[Whiteboard approach](https://docs.google.com/document/d/1cmeyXblya6MF4VQsuCDRnsRnr1KlDvfH3hycpl7nVGU/edit?usp=sharing)

### PROBLEM DOMAIN
Given two ordered lists, return a list with all the elements sorted.

### VISUALS
INPUT
[10,15, 20,25,30]
[1,3,5]

OUTPUT
[1,3,5,10,15,20]



### EDGE CASES
- Input can have different lenght.
- Input is sorted.
- I should not use build in functions.


### ALGORITHMS

#### APPROACH 1,

```
create a function that receives 2 arrays
	add basic validations on the arrays
	create an empty return list
	create 1 ponter for list 1, and set to 0
create 2 ponter for list 2, and set to 0
	create a while for pointer1 < len(array1) and pointer2< len(array2)
		if array[pointer1] < array[ponter2]:
			result.append(array1[ponter1])
			pointer1 +=1
		else:
			result.append(array2[ponter2])
			pointer2 +=1

	# if there are more elements in the array to be checked, add the to the list
while pointer1 < len(array1):
	result.append(array1[pointer1])
pointer1 +=1

while pointer2 < len(array2):
	result.append(array1[pointer2])
pointer2 +=1

return result


```


#### TESTS
```
[10,15, 20,25,30]
              ^
[1,3,5]
     ^

OUTPUT
[1,3,5,10,15,20]
```


#### BIG O
**Time O(n):** I'm passing only once.

**Space O(nm):** I'm creating a new ds with all the elements of n and m.

### CODE
[cracking_practices/join_two_lists/join_two_lists.py](join_two_lists.py)


### TESTS
[tests/test_join_two_lists.py](../../tests/test_join_two_lists.py)

### GITHUB BRANCH

[Pull Request 32, Branch: join_two_lists](https://github.com/ilealm/cracking-practices/pull/32)
