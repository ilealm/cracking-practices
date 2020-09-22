[Table of Contents](../../README.md)


# Check Subtree 4.10

[Whiteboard approach](https://docs.google.com/document/d/1PwFdHefgIPOlYBHEE95LvBuLp14a2k5XeDJLXqCEg1g/edit?usp=sharing)

### PROBLEM DOMAIN
T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the new two trees would be identical.


### VISUALS
Please refer to Whiteboard approach


### EDGE CASES
- T2 can be a subtree of T1, but not otherwise.
- What identical means? The same values and levels?
- The subtree can be at any depth this means, the subtree T2, in T1 could have nodes below.
- T1 can not be a subtree of T2
- T2 can appear several times on T1, but with one appearance is enough.
- I can assume I have node, binary tree, deque classes.
- T2 can not be a complete or balanced tree.
- I can have duplicates.



### ALGORITHMS

#### APPROACH 1,
- Traverse tree1 in BreadthFirst, and compare each node to the root of tree2, if both values are equal, then review if are same trees.

```
create a function that receives 2 trees
	traverse t1 in BreadthFirst fashion
		if the value of current node is equal to the value of t2.root

		call helper function are_equal and send current and t2.root
		if result of are_equal is true, return true

	return False

create function are_equal which receives two tree(t1, t2)
	declare are_eral_flag to true
	declare bf_t1 tp queue()
	declare bf_t2 tp queue()
	traverse both tree in BreadthFirst simuntanisly, while the queue is not empty, and are_eral_flag is true
		compare value of front of t1 to value of front2
			if are not equal:
				return False

	return True


```


#### TESTS
```
reviewing: 100,50,150,25,75,175
t2.root: 175

now in function are_equal
are_eral_flag = True
queueT1: 175,160, 190, 151, 165, 180, 200
queueT2: 175,160, 190, 151, 165, 180, 200
```


#### BIG O
**Time O(nLogn):** In work case scenario, I will traverse all the nodes, and I may check in tree2 several times.
**Space O(1):** I'm not creating new ds.

### CODE
[cracking_practices/check_subtree/check_subtree.py](check_subtree.py)


### TESTS
[tests/test_check_subtree.py](../../tests/test_check_subtree.py)

### GITHUB BRANCH

[Pull Request # n, Branch: check_subtree](https://github.com/ilealm/cracking-practices/pull/X)
