[Table of Contents](../../README.md)



# Problem 2.4: Partition

[Whiteboard approach](https://docs.google.com/document/d/1CWpWiwpGs_L9CbaFV9s14Td3ViSMUYz7OBzTlDLZpa8/edit?usp=sharing)

### PROBLEM DOMAIN

Write code to partition a linked list around a value X, such that all nodes less than X come before all nodes greater than or equal to X. If X is contained within the list, the value of X only needs to after the element less than X. The partition element X can appear anywhere in the "right partition", it does not need to appear between the left and right partitions.

### INPUT
13 -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> None
partition : 5

### OUTPUT
3 -> 1 -> 2 -> 10 -> 13 -> 5 -> 5 -> 8

### EDGE CASES
- The partition can or not be in the LL.
- I don't need to order the values of the LL.

### ALGORITHMS

#### APPROACH 1, Function: partition
**_I like this approach the most_**

I'm going to obtain traverse all the ll, if the current node.value >= partition, I will remove it and appending to the same ll, without losing the link of the nodes before. If I need to append, I will get the tail only once, and updating it on each append. Also, I'm using a pointer to the first appended node, so I don't re visit them.

```
create a function that receives a LL head and a partition value.
add basic validations on the LL and partition
set before = none
set current = ll.head
set ll_tail = none
set pointer_appened = none
traverse while current is truly
     if current == pointer_appened
           exit while
       if current.value >= partition:
           if not ll_tail then set ll_tail to helper function get_ll_tail(ll)

           # unlink from the ll and re linkit to the end of the ll
           save the next position of the ll, set after = current.next
		   save the link if there are nodes before the current, and link to the next node
           if there are no nodes before, set ll.head to the next node
           breack the link of the current node

           if not pointer_appened, set to the current node
		   move the ll.tail
           ll_tail.next = current
           ll_tail = current
       else
	         set before as the current node
		   set after as the current.next

       move to the next node

   return ll


# Returns the last node of the given ll
create a function that receives a ll
traverse the ll until current.next = none
return current
```


#### TESTS
partition: 5
current: 13, 8
before: none, 13, 3, 5
head: 13, 3

input
     13 -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> None
     	            C^
               B^
          H^
output
13 -> none
5 -> none
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> -13 ->None
H^


#### BIG O
**Time O(n):** I need to traverse all the LL. Helper function get_ll_tail will have O(n)

**Space O(1):** I'm not creating a new data structure here.

_______

#### APPROACH 2, Function: partition_new_ll

This is the simplest solution. It traverses the original ll and for each value, it appends / insert in a new list, and returns that new list. Not great because it creates a new data structure of the same length of the original.

```
create a function that receives a LL head and a partition value.
add basic validations on the LL and partition
set current to the ll.head
create a new ll
traverse while current is valid
if the value of current >= partition
		append current.value to new ll
else
 	insert current.value to new ll

  set current = current.next

return return_ll
```
#### BIG O
**Time O(n)**: we are traversing all the list.

**Space O(n)**: We are creating a copy of the LL.

_______

#### APPROACH 3, Function: partition_append_just_greater_or_equals

This approach traverses the ll and checks if current.value >= partition, if so, this node
is removed from the ll and put in a temporary list (which only refers the node, so no new ds is created) and at the end of the traverse, the temp list is appended to the end of the list.
With this approach, we ensure we only traverse the original list once, and not re traverse nodes that had already visited. We are not creating new ds because we are re assigning the values of the nodes. Is similar to approach 1, but it manages the nodes differently.

```
create a function that receives a LL head and a partition value.
add basic validations on the LL and partition
set current to the ll.head
set temp_ll_head equals to None
set before = None
traverse while current
       set after = current.next
       if current.value >= partition:
           # before unlink, I need to save whatever I have before in the ll
           if not before == None:
               set before.next = current.next
           # unlink this node to the original ll
           if current == ll.head:
               set ll.head = current.next
           if before == None:
               set ll.head = after
           current.next = None
           # link this node to the temp_ll
           if temp_ll_head == None:
               temp_ll_head = current
           else:
               current.next = temp_ll_head
               temp_ll_head = current
       else:
		set before = current


move to the next node: current = after

  dd the temp ll to current.next
   before.next = temp_ll_head

   return ll

```

#### BIG O
**Time O(n):**
- I'm traversing all the list.

**Space O(1):**
- I'm re assigning pointers, not creating new data structrure.
