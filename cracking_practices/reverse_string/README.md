[Table of Contents](../../README.md)


# Problem Reverse String

[Whiteboard approach](https://docs.google.com/document/d/1GuxlHG6jJIGliP20J77rbbujBBpPo_9rnODHEtXPL1w/edit?usp=sharing)

### PROBLEM DOMAIN
Given a string, return it in reverse order.

### VISUALS
```
INPUT                   OUTPUT
the dog is sleeping		gnipeels si god eht
hi				        ih
a				        a
```


### EDGE CASES
- The string can contain any character.
- The string can contain any amount of words.
- The string can be any length.
- It will be case insensitive.



### ALGORITHMS

#### APPROACH 1,reverse in place.
BUT Python does not allow you to swap out characters in a string for another one; strings are immutable.
```
create a function that receives a string
add basic validation of the string
create a variable "right" and set the value of len(word)-1
create a variable "middle" and set the value of right // 2
create a loop "left" from 0 to middle:
	swap word[left] and word[right]
	set right equals right - 1

return string
```


#### TESTS
```
string: bunny, yunnb, ynnub
right = 4, 3
middle = 2
left = 0, 1
```


#### BIG O
**Time O(logn):** Because I'm traversing only the half of the string.

**Space O(1):** I'm creating the same new variables.


#### APPROACH 2 create a new variable.

```
create a function that receives a string
add basic validation of the string
create a new return variable (srt_to_return) and set to nothing
create a loop from 0 to lenght of string:
	set srt_to_return = string[i] + srt_to_return

return srt_to_return
```

#### TESTS
```
string: bunny
i           ^
srt_to_return = '', b, ub, nub, nnub, ynnub
```

#### BIG O
**Time O(N):** Because I'm traversing all the nodes

**Space O(N):** O(n) Because I'm creating a new ds.

### CODE
[cracking_practices/reverse_string/reverse_string.py](reverse_string.py)


### TESTS
[tests/test_reverse_string.py](../../tests/test_reverse_string.py)

### GITHUB BRANCH

[Pull Request # 16, Branch: reverse_string](https://github.com/ilealm/cracking-practices/pull/16)
