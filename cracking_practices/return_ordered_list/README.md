[Table of Contents](../../README.md)


# Problem: Return Ordered List

[Whiteboard approach](https://docs.google.com/document/d/103_98EJXfaNryVCxI_frsDvGwLWjVIrtoj9WqQhb-Ac/edit?usp=sharing)

### PROBLEM DOMAIN
Having a list of thousands of unordered numbers from 1 - 100, return an ordered list with all these values in order.

### INPUT, Example
[ 30, 50, 90, 34, 67, 30, 2, 90, 70 ]

### OUTPUT, Example

[ 2, 30, 30, 34, 67, 50, 70, 90, 90 ]



### EDGE CASES
- Numbers can be repeated n times.
- Maybe missing numbers in the sequence.
- The function must return all the values, not just the ones that appear.
- I can assume I have a node and LinkedList object, and node objects have also a counter attribute.



### ALGORITHMS

#### APPROACH 1, Implement a linked list
- Implement a link list (ll) to save on ordering fashion the values, and each node will have a counter of the occurrence of that number. At the end traverse the ll and return a list.
Pros: traversing the LL to find values will be faster
Cons: I will create a new DD to store in worst-case scenario 100 nodes. and then create a new list to return the values in order way.

#### visuals

```
Input
[ 30, 50, 90, 34, 67, 30, 2, 90, 70 ]

numbers_ll =
[2, counter=1] →  [30, counter=2]→ [value=34, counter=1]→ [value=67, counter=1]→ [value=50, counter=1]→ [value=70, counter=1]→ [value=90, counter=2]→None

Output
return_list = [ 2, 30, 30, 34, 67, 50, 70, 90, 90 ]
```

#### ALGORITHM
```
create a function that receives a list with n elements(list)
	create a ll object (ll_numbers)
create an empty array (return_list)
create a current variable and set to ll.head
create previous variable and set to none
loop through list (i)
	# the ll is going to be empty the 1srt time, so insert list[0] as the head
	if not head:
		create a node with value list[i]
		set head to this new node
		break

traverse ll until current is valid:
		if current.value is equals to list[i],
			increase by 1 current.counter
			break
		if current.next.value is greater than list[i]
			create a node with value list[i]
			set new node.next to current.next
			set current.next to new node
			break

		# if I didn't find the value, I need to apped it to the end, but I need to check if goes before / after the last node.
		if not current.next:
create a node with value list[i]
			if current.value is greater than list[i]:
				set new node.next to current
				if not previous:
					set ll.head = new node
				else
					set previous.next = new node
		set current.next to none #already should be pointing to none
				break
			else
				create a node with value list[i]
				set current.next = new node
			break



		set previous to current
		set current to current.next


# create return list
set current = ll.head
traverse ll while current is valid
	create a loop from 0 to current.counter
		append in return_list, current.value
	set current equals to current.next

	return return_list
```

#### TESTS
```
TEST
  	 0   1     2    3    4   5
list[i]: [ 30, 50, 90, 34, 90, 70 ]
i =                             ^


                  head
current:[value:30, counter:1]→[value:34, counter:1]→ [value:50, counter:1]→ [value:90, counter:1]→None
current
```

#### BIG O
**Time O(n^n):** Because I need to traverse all the list, and for each element, I will traverse the linked list.

**Space O(n):** Because I'm creating 2 new ds of the size of n.


#### APPROACH 2, Implement a Binary Seach Tree
Instead of a LL, have a binary tree with also a counter on each node, traverse it to find the right position, and update the node.counter or insert to left or right. In the end, traverse the tree inorder and insert into return array the value n times.

_* I will implement the binarySearchTree class that I already created._

#### ALGORITHM
```
add to node class a counter property
	       self.counter = 1

update binarySeachTree.add method, so when the node already exists, just increase by one counter method
if current_node.value == new_node.value:
               current_node.counter += 1
               return

update inorder method so the value will be inserted in the list counter times

           for i in range(0, current_node.counter):
               list_return.append(current_node.value)
```



#### BIG O
**Time O(nlogn):** Because I need to traverse all the list, and for each element, I will traverse the half of the tree.


**Space O(n):** Because I'm creating 2 new ds of the size of n in worst-case scenario.




### CODE
[cracking_practices/return_ordered_list/return_ordered_list.py](return_ordered_list.py)


### TESTS
[tests/test_return_ordered_list.py](../../tests/test_return_ordered_list.py)

### GITHUB BRANCH

[Pull Request # 17, Branch: return_ordered_list](https://github.com/ilealm/cracking-practices/pull/17)
