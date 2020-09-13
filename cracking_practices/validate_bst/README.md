[Table of Contents](../../README.md)


# Problem Validate BST 4.5

[Whiteboard approach](https://docs.google.com/document/d/1wfEgqLhknxqgjuOXv3Hw_caKXiCHAKNEU_hyHbfcbiw/edit?usp=sharing)

### PROBLEM DOMAIN
Implement a function that checks if a binary tree is a BST.

### VISUALS
```
INPUT
A tree
            100
	    /         \
	50	          150
   /
  25

OUTPUT
True


INPUT
A tree
           100
	    /       \
	50	         150
    /         /     \
  25        10       180

OUTPUT
False
```


### EDGE CASES
- The node values can have just letters or just numbers.
- The tree can be any hight.
- Can be an unbalanced tree.
- The tree can have duplicates.
- I can assume I have access to BinarySearch Tree class.



### ALGORITHMS

#### APPROACH 1,  get left max, right min and compare to root.

```
create a funtion called validate_bst which receives a tree
	basic validations on tree
	call helper function get_max on root.left
	call helper function get_min on root.right
	compare get_max to tree.root, if get_max is greater, return False
	compare get_min to tree.root, if get_min is lower, return False
	return True

create helper function get_max_value which receives a node
validate node
set variable max_value to current.value

	create recursive function traverse which receives a node (current)
declare max_value as nonlocal to have access outside the recursive
add base case: if not current then return

		compare current.value > max_value, if true, change max_value to current_value

			if current has left, traverse it
		if current has right, traverse it

		call traverse function and send current
		return max_value


create helper function get_min_value which receives a node
validate node
set variable min_value to current.value

	create recursive function traverse which receives a node (current)
declare min_value as nonlocal to have access outside the recursive
add base case: if not current then return

		compare current.value < min_value, if true, change max_value to current_value

			if current has left, traverse it
		if current has right, traverse it

		call traverse function and send current
		return min_value

```


#### TESTS
```
            100
	    /        \
	   50	     150
     /   \       /
  25	   75	25


get_max (50….)
max_value: 50, 25

get_min_value(150…)
min_value: 150, 25


root: 100

root > max_value(25) : TRUE
root < min_value(25) : FALSE
```


#### BIG O
**Time O(n):** I'm traversing all the tree only once.
**Space O(1):** I'm creating the same local variables each time.

### CODE
[cracking_practices/validate_bst/validate_bst.py](validate_bst.py)


### TESTS
[tests/test_validate_bst.py](../../tests/test_validate_bst.py)

### GITHUB BRANCH

[Pull Request # 26, Branch: validate_bst](https://github.com/ilealm/cracking-practices/pull/26)
