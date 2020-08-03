[Table of Contents](../../README.md)


# Problem  2.8 : Loop Detection

[Whiteboard approach](https://docs.google.com/document/d/14doAYLKDE5OvWw32x-CGslI7j6VcnknSV-nZBiGOXlI/edit?usp=sharing)

### PROBLEM DOMAIN
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

### INPUT, Example 1
A -> B -> C -> D -> E -> C (the same C as earlier)

### OUTPUT, Example 1

C

### EDGE CASES
- Each ll can or not have a loop.
- Each ll can have different lengths.
- If the circular list doesn't contain a loop, return False.


### ALGORITHMS

#### APPROACH 1: Traverse the circular ll and have a set containing visited nodes, if the current node exists in the set, return it and break the traverse.


```
create a function that receives one cirular linked list (cirular_ll).
add basic validations on the cirular_ll.
create a current variable and set to cirular_ll.head
create a variable circular_set and set to empty.
traverse while current is valid
	check if current exists circular_set, if so:
		return current

	insert current into circular_set
	move current to current.next

	return False

```


#### TESTS
```
A -> B -> C -> D -> E -> C
                         C^

current (C^):

circular_set= A, AB, ABC, ABCD, ABCDE
```


#### BIG O
**Time O(n):** Because in the worst-case scenario I'm traversing all the circular linked list.


**Space O(n):** Because I'm creating a new data structure with the copy of cirular list (n).


### CODE
[cracking_practices/loop_detection/loop_detection.py](loop_detection.py)


### TESTS
[tests/test_loop_detection.py](../../tests/test_loop_detection.py)

### GITHUB BRANCH


[Pull Request # 5, Branch: loop_detection](https://github.com/ilealm/cracking-practices/pull/5)
