[Table of Contents](../../README.md)


# Problem 4.5: Sum List
[Whiteboard approach](https://docs.google.com/document/d/1rjC8V7h_KN9GAm-5j0JyfK1WZnCO-tQW9X22_LdGpGI/edit?usp=sharing)

### PROBLEM DOMAIN

You have 2 numbers represented by 2 linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1st digit is at the head of the list. White a function that adds the 2 numbers and returns the sum as a linked list.

### INPUT
7 -> 1 -> 6 -> None


5 -> 9 -> 2 -> None

### OUTPUT
617 + 292 = 912

### EDGE CASES
- I can assume I can call LinkedList methods.
- The nodes contain a positive digit.
- The length of the linked list can vary.

### ALGORITHMS

#### APPROACH 1
I have 3 main tasks:
1. for each link list, traverse and save the values in a variable in the right order
1. sum the result, and store it in reverse order
1. convert the result to a linked list

```
create a function that receives two linked list as a parameters (sum_list).
add basic validation to the lists
create a helper function that will receive a linked list and will traverse it, and returns the values of the nodes in reverse order and in string format: get_values_in_reverse()
call my helper function for each linked list, and store the return in a variable.
convert the values of the return of the linked list to an integer.
sum the values of the linked list and store it in a variable.
convert the sum value to a string.
create a new empty linked list (return_ll)
loop in the sum string, and for each position, insert in the return_ll.
return_ll



get_values_in_reverse:
receive a linked list
create a variable current and set to ll.head
create a string empty variable: ll_values
traverese ll while truly
	set ll_values = conver to string(current.value) + ll_values
	move current to the next node

return ll_values

```

#### TESTS

get_values_in_reverse()

current[ C^ ] :

ll_values: 7, 17, 617

7 -> 1 -> 6 -> None

          C^

current[ C^ ] :

ll_values: 5, 95, 295

5 -> 9 -> 2 -> None

          C^


sum_list()

return_ll -> None

first_ll_value = 617

second_ll_value = 295

ll_sum = str(int(617) + int(295))  => 912


return_ll = 9 -> None

return_ll = 1 -> 9 -> None

return_ll = 2 -> 1 -> 9 -> None



#### BIG O
**Time O(n):**
- I need to traverse all both linked list. For the insertion on the new linked list, the time will be O(1).


**Space O(n):**
- I'm creating a new data structure for my return linked list.

