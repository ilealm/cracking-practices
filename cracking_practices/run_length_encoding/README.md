[Table of Contents](../../README.md)


# Problem: Run Length Encoding

[Whiteboard approach](https://docs.google.com/document/d/1i43Q4TKveuODiBX1T2QS0x_21xca5uBK_a513cS9P9U/edit?usp=sharing)

### PROBLEM DOMAIN
Create a function that receives a string and returns the run-length encoding of it.

### VISUALS
```
INPUT               OUTPUT
aaabbcccca 		    3a2b3c1a
aaaaaaa 			7a
abcd				1a1b1c1d
```

### EDGE CASES
- The length of the string can be any length.
- I can have any character as input.
- The return will be a string.

### ALGORITHMS
Traverse all the string and have a past character, if it is different from the current character, I will append the past character and the counter to the return value, and then reset my counter and last character.

```
create a function that receives a string
add basic validations to the string
create a counter variable and set to 0
create a previousChr variable and set to string[0]
create returnString and set to ''
traverse the string
	for each possition, I will check it (current) against previousChr,
if are the same,
add 1 to counter
else
	add counter to returnString
	add previousChr to returnString
	reset counter to 1
	set previousChr = current character

# add the last run of the string
add counter to returnString
add previousChr to returnString

return returnString


```


#### TESTS
```
aaabbcccca
         ^
counter = 0, 1,2,3, 1,2, 1,2,3,4, 1
previousChr = a,b c
returnString = '',3,3a, 3a2, 3a2b, 3a2b4, 3a2b4c, 3a2b4c1a

```


#### BIG O
**Time O(n):** I'm traversing all the input string.

**Space O(n):** I'm creating a new data structure (returnString) that can be bigger than the original input, in the case when there are not consecutive duplicated characters.


### CODE
[cracking_practices/run_length_encoding/run_length_encoding.py](run_length_encoding.py)


### TESTS
[tests/test_run_length_encoding.py](../../tests/test_run_length_encoding.py)

### GITHUB BRANCH

[Pull Request # 6, Branch: run_length_encoding](https://github.com/ilealm/cracking-practices/pull/6)
