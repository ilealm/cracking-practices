[Table of Contents](../../README.md)

# Problem

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN

* Implement a graph class with methods add, delete, add edge, remove edge, print edges.
* Implement Breath traverse.
* Implement topological sort.
* Implement a method to determinate is the graph has a cycle.

### VISUALS

```
A --> B
B --> C
C --> D


or

A --> B
A --> C
B --> C
C --> A

// here are ALL the nodes
NODES (hash table)
   label : node
   A : <obj 1934>
   B : <obj 4572>
   C : <obj 2242>


ADJ_LIST (hash table)
    node : list[all the nodes with edges. AKA neighbors]
    <obj 1934> : [<obj 4572>, <obj 2242>]
    <obj 4572> : [<obj 2242>]
    ...

```

### EDGE CASES

- I can have valid values in the arays.
- Values can be repeted.

### ALGORITHMS

```
Please review the code.
```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to

**Space O(n):** I'm

### CODE

[cracking_practices/graphs/graphs.py](graphs.py)

### TESTS

[tests/test_graphs.py](../../tests/test_graphs.py)

### GITHUB BRANCH

[Pull Request # n, Branch: x_x](https://github.com/ilealm/cracking-practices/pull/110)
