[Table of Contents](../../README.md)


# Problem fibonacci

[Whiteboard approach](https://docs.google.com/document/d/1qnLcW2MVoxmZSqAiYUko8g7RmzxnYD7PuvBuVVlYGL8/edit?usp=sharing)

### PROBLEM DOMAIN
Given a number, return its value in the fibonacci sequence. Fibon

### INPUT, Example 1

given 6 => 8

N 0, 1, 2, 3, 4, 5, 6, 7
  0  1  1  2  3  5  8  13…


### EDGE CASES
- n must be greater than 0.
- n must be an integer.

### ALGORITHM
```
create a recursive function that receives an integer number: fibonacci(n)
	create base case: if n is equal or less than 2, return 1
	return fibonacci -1 + fibonacci -2
```


#### TESTS
```
Given 6

fibonacci(6)
fibonacci(5)
	fibonacci(4)
		fibonacci(3)
			fibonacci(2)
			fibonacci(1)
		fibonacci(2)
	fibonacci(3)
		fibonacci(2)
		fibonacci(1)
fibonacci(4)
fibonacci(3)
		fibonacci(2)
	fibonacci(1)
fibonacci(2)

```


#### BIG O
**Time O(2^n):** The function is called twice, n times.
**Space O(1):** I'm not creating a new ds.

### CODE
[cracking_practices/fibonacci/fibonacci.py](fibonacci.py)


### TESTS
[tests/test_fibonacci.py](../../tests/test_fibonacci.py)

### GITHUB BRANCH

[Pull Request # 15, Branch: fibonacci](https://github.com/ilealm/cracking-practices/pull/15)
