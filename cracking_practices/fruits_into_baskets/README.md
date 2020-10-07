[Table of Contents](../../README.md)


# Problem Fruits into Baskets

<!-- [Whiteboard approach](X) -->

### PROBLEM DOMAIN
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

### VISUALS
```
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
```
### EDGE CASES
- Can be any characters.
- Array can be any lenght.


### ALGORITHMS

#### APPROACH 1, Sliding window

```
create a function that receives an array(fruits)

    declare a set to control the diffent trees I can have (2)
    declare a string variable to store the current substring (sub_fruits)

    create a loop for all the elements in the array
        add current element to sub_fruits
        check if I'm changing tree (if I aleady have 2 types in my basquets)
            if so, I'm going to remove the oldest tree
                recreate the current fruits set
            else:
                add the current fruit to the set

```


#### TESTS
```
sub_fruits = cac
current_fruits = ca

```


#### BIG O
**Time O(n):** I only travese the array 1.

**Space O(n):** My variable substring could be n size.

### CODE
[cracking_practices/fruits_into_baskets/fruits_into_baskets.py](fruits_into_baskets.py)


### TESTS
[tests/test_fruits_into_baskets.py](../../tests/test_fruits_into_baskets.py)

### GITHUB BRANCH

[Pull Request # 39, Branch: fruits_into_baskets](https://github.com/ilealm/cracking-practices/pull/39)
