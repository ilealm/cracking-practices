[Table of Contents](../../README.md)


# Problem Successor 4.6

[Whiteboard approach](https://docs.google.com/document/d/1T5yDSShFOiUkRoYeFtC3wpJQeGdja-DcFpLNrUFMu_Y/edit?usp=sharing)

### PROBLEM DOMAIN
Write an algorithm to find the "next" node (i.e in-order successor) of a given node in a BST. You may assume that each node has a link to its parent.


### VISUALS
input, a tree and a node or a value ??
node = 75, the next node is 90?
what happens if there no right?, return that node?, false? None?

INPUT: node 75.
OUTPUT: 80

INPUT: node 150.
OUTPUT: 151

INPUT: node 15.
OUTPUT: 20

INPUT: node 165.
OUTPUT: None



### EDGE CASES
- By next, I refer the next greater? to one to the right?
- The tree won't have duplicates.
- The values are added following the rule that lower values to the left, greater to right. So the next must be at the right subtree.
- Can be an unbalanced tree.
- The nodes also have a link to the parent node. Only root will have parent = None
	node(): value, left, right, parent


### ALGORITHMS

#### APPROACH 1. From the input node, and from there, get the right node, then most left node value.
```
create a function that receives a node

	set successor to None
	create a inside function called traverse, to get to the left-most node
	send traverse(node.right)
	return successor

	create helper inside function: traverse, which receives a node (current)
		set successor as nonlocal
		add base case to exit the recursion
			if current is not truty, return
			if current has left, recurse on it:
				traverse(current.left)
			else
				#I got to the left-most node
				set successor to current

```


#### TESTS
```
INPUT:150
successor: None, 151
current: 175,160,151
```

    
#### BIG O
**Time O(Logn):** I'm traversing at most, half of the tree.

**Space O(1):** Because I have the same local variables always.

### CODE
[cracking_practices/successor/successor.py](successor.py)


### TESTS
[tests/test_successor.py](../../tests/test_successor.py)

### GITHUB BRANCH

[Pull Request # n, Branch: successor](https://github.com/ilealm/cracking-practices/pull/X)
