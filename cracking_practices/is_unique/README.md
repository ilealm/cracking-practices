[Table of Contents](../../README.md)


# Problem 1.1 : Is unique

[Whiteboard approach](https://docs.google.com/document/d/1U00aX7OK1_CAA7pCiKLgHuM82wqjB6zC8tQUGZ4QPxg/edit?usp=sharing)

### PROBLEM DOMAIN
Implement an algorithm to determinate if a string has all unique characters

### INPUT
```
abcde     	→ True
abac		→ False
a		    → False
a1b2 ir	    → True
```


### EDGE CASES
- I can accept any character.
- The string can be any length.
- Any character can be n times in the string.
- Can accept empty strings


### ALGORITHMS

#### APPROACH 1,
- Have 2 pointers, 1 will point to the current letter I'm checking, and the second will be a runner that will check form current to the end of the string, or to the first occurrence equals to current.

```
create a function that receives an string
	if the string is empty, return False
	create a loop from 0 to len(string)-2 → because I'm having a runner. this is current loop
		create a inner loop from current+1 to len(string) -current-1
			compare current vs runner, if they are the same
				return False

	return True


```


#### TESTS
##### Test 1
```
0123
 abcde
   c^
    r^

Current(c^):a,b,c
Runner(r^):b,c,d,e,c,d,e,d,e
return: True

```

##### Test 2
```
 0123
 abac
c^
  r^

Current(c^):a,
Runner(r^):b,a
return: False

```

#### BIG O
**Time O(n^2):** Because I need to traverse all the positions and for each possition, I do an inner loop for the rest of the elements.

**Space O(1):** I'm not creating new ds.

### CODE
[cracking_practices/is_unique/is_unique.py](is_unique.py)


### TESTS
[tests/test_is_unique.py](../../tests/test_is_unique.py)

### GITHUB BRANCH

[Pull Request # 7, Branch: is_unique](https://github.com/ilealm/cracking-practices/pull/7)
