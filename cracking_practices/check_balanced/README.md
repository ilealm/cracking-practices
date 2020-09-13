[Table of Contents](../../README.md)


# Problem Check Balanced 4.4

[Whiteboard approach](https://docs.google.com/document/d/1rl-HlzNHCb90uE_B6Q5ChWTlc45N2wCbFx5b5mIbPmw/edit?usp=sharing)

### PROBLEM DOMAIN
Implement a function to check if a binary tree is balanced. For the purpose of this question, a balanced tree is defined to be a tree such as the hights of the two subtrees of any node never differ by more than one.

#### what makes a balanced tree?
- each node has at most two children.
- when starting at the root of the tree, the levels of right and left can deffer at must by one.
- the number nodes of each level of left and right can deffer


### VISUALS

INPUT
```
           100
         /      \
      50		150
     /  \
   25   40
```
OUTPUT
False

### EDGE CASES
- the input tree is a binary tree.
- the tree can have duplicates.
- the tree can be unbalanced.
- the tee can be any hight.
- the unbalanced part could be in a subtree of left or right.
- if the tree is empty, return False
- for this exercise, I can assume I have a Queue class



### ALGORITHMS

#### APPROACH 1
- Get the num of the level to root.right and root.left, and if the difference is > 1, return False, el return true.

```
ALGORITHM
create function get_hight which receives a tree:
add basic validations to the tree

	if the tree have left,
call helper function get_hight on tree.left and to variable left_height
otherwise
set left_height = 0

	if the tree have right,
call helper function get_hight on tree.right and to variable right_height
otherwise
set right_height = 0

	# compare the heights
	if (left_height - right_height ) is equal to 0 or 1
       return True
else
       return False


create function get_hight which receives a tree
	set variable num_levels to 0
	declare a queue variable current_level
	declare a queue variable next_level

	enqueue the tree into current_level

	create a loop while current_level is not empty
		set variable front to current_level.dequeue
		if front have left, enqueue into next_level
		if front have right , enqueue into next_level

		#check if I need to change level
		if current_level is empty
           increase num_levels by one
		swap current_level and next_level

	return num_levels

```


#### TESTS
```
          100
        /      \
      50		150
     /  \
   25   40

left_height:
right_height:

LEFT
num_levels: 0,1,2

current_level:50, 25,40
next_level:25

RIGHT
num_levels: 0,1,2

current_level:50, 25,40
next_level:0,

RETURN: FALSE

```


#### BIG O
**Time O(n):**  Because I'm traversing only once.

**Space O(1):** Because I'm creating the same variables every time

### CODE
[cracking_practices/check_balanced/check_balanced.py](check_balanced.py)


### TESTS
[tests/test_check_balanced.py](../../tests/test_check_balanced.py)

### GITHUB BRANCH

[Pull Request # 27, Branch: check_balanced](https://github.com/ilealm/cracking-practices/pull/27)
