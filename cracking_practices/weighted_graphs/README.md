[Table of Contents](../../README.md)

# Problem

Implement Dijkstra's algorithm to find the sortest path in a weigted graph.

Also, detect a cycle in undirected graphs.

### PROBLEM DOMAIN

### VISUALS

```
     1
A  ------ B

     10
A  ------ C

     2
B  ------ C

Find the shortest path from A to C

>> A, B, C

```

### EDGE CASES

- Empty graph.
- Only possitive values.

### ALGORITHMS

```
Use breath first from starting node, from there, traverse each neighbor, while keeping tracking on which node had been visited. Also, keep track of the distances and the parent of each node.

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to

**Space O(n):** I'm

### CODE

[cracking_practices/weighted_graphs/weighted_graphs.py](weighted_graphs.py)

### TESTS

[tests/test_weighted_graphs.py](../../tests/test_weighted_graphs.py)

### GITHUB BRANCH

[Pull Request # n, Branch: weighted_graphs](https://github.com/ilealm/cracking-practices/pull/X)
