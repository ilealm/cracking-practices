[Table of Contents](../../README.md)


# Problem: Binary Tree Zig Zag.

[Whiteboard approach](https://docs.google.com/document/d/1-9eUTuEyqJKBEYzV3OqvdquukBZkqu0e4SthqdJjUJw/edit?usp=sharing)

### PROBLEM DOMAIN
Having a binary search tree, return the values in a zig zag fashion.


### INPUT
![](../../assets/zig_zag_tree.png)



### OUTPUT

[100, 150, 50, 25, 75, 125, 175, 190, 160, 140, 115, 90, 60, 40, 15, 5, 20, 30, 45, 55, 65, 80, 95, 110, 120, 130, 145, 150, 165, 180, 200]


### EDGE CASES
- The tree can be N levels.
- The tree can be unbalanced.
- All the nodes will be returned in the list.
- The value of the nodes are irrelevant.
- The zig-zag movement starts from the root to the right.
- I can assume I already have the class node, BST, binaryTree, and BreadthFirst.
- Tree is mostly balanced.



### ALGORITHMS

#### APPROACH 1,BRUTE FORCE. Is NOT the most efficient way, but is the first approach.
- Traverse the tree in a breath way, save the traverse in a list, then move to that list and create a new list with the zipped values. Is NOT the most efficient way, but is the first approach.


```
create a function that receives a tree
implement basic validation on the tree
Call tree.breadthFirst to have all the tree values in a list (bf_list). I know which elements are in each level, using pow.

	# declare variables
	create zig_zag_list list and set to empty (here I will save the values of the traversing in zig-zag)
	create pointer variable and set to 0 (helper to move through the list)
create level variable and set to 0, (will tell me which level I'm now)
create variable starting_on_right and set to True, so I know which side to move.

	append the root into zig_zag_list
	move 1 position in pointer
	move 1 position in level

	create a loop, while len(zig_zag_list) is less than len(bf_list)
		calculate the possitions_to_move I need to move to left or right, by using pow(2, level)
validate if the possitions_to_move is less than the available elements in the bf_list, if so, recalculate possitions_to_move
		if starting_on_right:
			stablish the position on the right of the tree, where I'm moving to the left
			create a loop for the number of possitions to move
			append in zig_zag_list the right value from bf_list
				increase the ponter by one
			change flag starting_on_right to false
		else:
			create a loop for the number of possitions to move
append in zig_zag_list the right value from bf_list
				increase the ponter by one

			change flag starting_on_right to true

       increase level by 1


   return zig_zag_list


```


#### TESTS
```
bf_list =
[100, 50, 150, 25, 75, 125, 175, 15, 40, 60, 90, 115, 140, 160, 190, 5, 20, 30, 45, 55, 65, 80, 95, 110, 120, 130, 145, 150, 165, 180, 200]

level = 0,1,2,3,4
starting_on_right = T, F, T, F, T

zig_zag_list=
[100, 150, 50, 25, 75, 125, 175, 190, 160, 140, 115, 90, 60, 40, 15, 5, 20, 30, 45, 55, 65, 80, 95, 110, 120, 130, 145, 150, 165, 180, 200]

```


#### BIG O
**Time O(n2):** I'm traversing the tree to copy to a list, and then I move again trough the list.

**Space O(n2):** Because I'm reacting two new ds. (one to have the tree in breathFirst, and another to return the zig-zag)


-----

#### APPROACH  2, IMPLEMENTING BREADTH FIRST.

- Traverse the tree in a breath way, and create a temp list to save the nodes of each level. Depending on if the level is even or odd, the node will be appended to the end or inserted at the top of the temp list. When I change level, before doing that I will insert the temp list to my return list.


```
create a function that receives a tree
implement basic validation on the tree
	create a variable list list_breadth and set to empty list

	declare a queue instance (breadth)
enqueue the tree.root

set variable level, and set to 0
set num_ele_this_level to pow(2,level)
set ele_added_this_level to 0
set is_even_level = True
set temp_list to empty list

	create a loop while there is something in the queue
		set front to breadth.dequeue()
      if front.left have something,
      	     breadth.enqueue(front.left)
      if front.right is not None
      	     breadth.enqueue(front.right)


       if is_even_level, then  temp_list.append(front.value)
       else,            temp_list.insert(0, front.value)

	increase ele_added_this_level by 1

	#check if I changed level
       if ele_added_this_level == num_ele_this_level:
		increase level by 1
		add temp_list to list_breadth
empty temp_list

set the new elements of the level in num_ele_this_level
set ele_added_this_level to 0
switch value of is_even_level

	# validate if the tree is unbalance in the last level, if so, add the rest of the list
if ele_added_this_level < num_ele_this_level : add temp_list to list_breadth

   return list_breadth

```
#### BIG O
**Time O(n):** I'm traversing the tree only once.


**Space O(nLogn):** Because I'm reacting two new ds:one temp which have one level at time, and another with all the nodes of the tree.


-----

#### APPROACH 3, IMPLEMENTING BREADTH FIRST WITH TWO QUEUES.

- THIS IS THE BETTER APPROACH, THE TREE DOESN'T NEED TO BE BALANCED
- Traverse t Implement 2 queues, one for actual level and second for next level.
- Using a flag to know where to move: left_to_rigth, based on this flag, I can know if insert left or right next.
- Based on: https://www.youtube.com/watch?v=PwEmiE5u3tE
- But I did some changes

#### ALGORITHM
```
create a function that receives a tree
	add basic validations to the three
	declare helper variables:
list_return = []
list_level = []
	current_level = Queue()
next_level = Queue()
   	left_to_rigth = False

	enque tree.root into current_level

	create a loop while current_level is not empty
		create a variable front and set to current_level.dequeue()

		if front have a left node, add it to next_level queue
		if front have a right node, add it to next_level queue

		depending on the flow I'm inserting, I will insert[0] or append in my helper list

       	if current_level is, empty, means I need to change level
			add to list_return what I have in list_level
            reset list_level
           		change the flow of the zig zag (left_to_rigth )
			swap queues current_level, next_level to next_level, current_level

   return list_return

```

#### BIG O
**Time O(n):** I'm traversing the tree only once.


**Space O(nLogn):** Because I'm reacting two new ds:one temp which have one level at time, and another with all the nodes of the tree.




### CODE
[cracking_practices/zig_zag_tree/zig_zag_tree.py](zig_zag_tree.py)


### TESTS
[tests/test_zig_zag_tree.py](../../tests/test_zig_zag_tree.py)

### GITHUB BRANCH

[Pull Request # 22, Branch: zig_zag_tree](https://github.com/ilealm/cracking-practices/pull/22)
