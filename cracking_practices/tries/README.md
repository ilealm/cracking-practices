[Table of Contents](../../README.md)

# Problem

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN
Given a Trie where I have words saved, and given a sufix, return all the possible words that start with the prefix.



### VISUALS

```
Saved this words: car, card, care, egg, nothing, careless.


If I send the prefix car, the I will get: car, card, care, careless.


```

### EDGE CASES

- The word does not exist in the Trie.
- Empty prefix.
- Dupplicated words on the Trie.


### ALGORITHMS

#### APPROACH 1,

```
Find the node of the last letter of word in the Trie.
Check if the node is_end_of_word = True, if so, add it to a list of found words.
Traverse all the node's children, keeping record of the traversed letters
    Check if the node is_end_of_word = True, if so, add it to a list of found words.
Return the list of found words.

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(L):** I need to traverse all the word, and may be some more letters.

**Space O(n):** I may need to add all the words in the Trie to the list of found words.

### CODE

[cracking_practices/tries/tries.py](tries.py)

### TESTS

[tests/test_tries.py](../../tests/test_tries.py)

### GITHUB BRANCH

[Pull Request # n, Branch: tries](https://github.com/ilealm/cracking-practices/pull/103)
