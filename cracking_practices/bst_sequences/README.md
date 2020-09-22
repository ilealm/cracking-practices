[Table of Contents](../../README.md)


# Problem BST Sequence 4.9

[Whiteboard approach](https://docs.google.com/document/d/1VTlOc0F2A-Pjb7JxjHiUIwvJacrNs9EvI-QONP9xrcg/edit?usp=sharing)

### PROBLEM DOMAIN
A binary search tree was created by traversing a through an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have lead to this tree.

### VISUALS
```
INPUT:
a BinarySearchTree

      2
     /  \
    1    3

OUTPUT [2,1,3], [2,3,1]

```


### EDGE CASES
- The input tree can have h high.
- The tree is a binary search tree, with no duplicates.
- The tree can be unbalanced.
- The root must be always at position 0.



### ALGORITHMS

#### APPROACH 1
- Get all the nodes, except for the root, and store it in an array, and then perform permutations on it, and insert the root at position 0 on the end of each permutation.

```
create a function that receives a binary search tree
	traverse the tree in preorder fashion and store the result in an array, except for the root.

	perform permutation on each array, and on the result, append the root. store this result in an array

	return array of permutations


```

#### BIG O
**Time O(n!):** I need to create the permutations of the array

**Space O(n!):** I'm creating an array for each permutation.

### CODE
[cracking_practices/bst_sequences/bst_sequences.py](bst_sequences.py)


### TESTS
[tests/test_bst_sequences.py](../../tests/test_bst_sequences.py)

### GITHUB BRANCH

[Pull Request # 33, Branch: bst_sequences](https://github.com/ilealm/cracking-practices/pull/33)
