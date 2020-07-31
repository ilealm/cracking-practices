[Table of Contents](../../README.md)


# Problem 2.6: Palindrome in Linked List

[Whiteboard approach](https://docs.google.com/document/d/1MMAjUCT9-pt2LyOuAJ9YPmM2Kc-Sv1QQiQPCZcZaHgg/edit)

### PROBLEM DOMAIN
Implement a function to check is a linked list is a palindrome. Each node contains a letter of the word to check.

### INPUT
head
k -> a -> y -> a -> k -> None

### OUTPUT
True


### INPUT
head
a -> b -> c -> None

### OUTOUT
False


### EDGE CASES
- The linked list can contain any character.
- Originally, is a single linked list.
- I can have upper and lower cases.
- The function will be not case sensitive.


### ALGORITHMS

#### APPROACH 1, Traverse the list and create a variable with all the nodes.value.
- I'm traversing all the linked list.
- I'm creating a new data structure (variable to store the node values)
- I'm traversing again the new data structure (only to the half)


```
create a function that receives a linked list (ll)
add basic validation on the ll
create an empty variable to store the values of the nodes (word)
create a variable to manage the current node, and set it to ll.head
traverse while current is truly
	add current.value to word
	set current to current.next
obtain the middle of word
create a variable left and set to 0
create a variable right and set to len(word)-1
loop from 0 to middle
	comprare word[left] to word[right], both in lowercase if equal
		add 1 to left
		substract 1 to right
	else
		return False

return True

```


#### TESTS
head\
0    1    2    3    4\
k -> a -> y -> a -> k -> None\
                    C^\
     L^\
               R^       .\
word = '', k, ka , kay, kaya, kayak\
current: C^\
middle = 1\
left L^ = 0\
right R^ = 4


#### BIG O
**Time O(n^2):** I need to traverse all the LL, and then, again the half of the new word.

**Space O(n):** I'm creating a copy of the original linked list.

_______

#### APPROACH 2, Change the linked list to a doubly linked list, and compare head to tail and move pointers to each other.

- I'm only traversing half of the linked list, which will be more efficient.
- I'm not creating a new data structure.
- I'm going to assume the list is already a double linked list.


```
create a function that receives a linked list (ll)
add basic validation on the ll
create an empty variable left to store the value of the head
create an empty variable right to store the value of the tail
Traverse the linked list until left and right are at the same node
	if left.value is not equal to right.value, both in lowercase
		return false
	else
		set left to left.next
		set right to right.previous
return True

```
#### BIG O
**Time O(n)**: I'm are traversing all the list, half from one side, and half from another side.

**Space O(1)**: I'm not creating new data structures.

### CODE
[cracking_practices/palindrome_ll/palindrome_ll.py](palindrome_ll.py)


### TESTS
[tests/test_palindrome_ll.py](../../tests/test_palindrome_ll.py)
