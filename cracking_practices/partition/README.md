[Table of Contents](../../README.md)


[Whiteboard approach](https://docs.google.com/document/d/1CWpWiwpGs_L9CbaFV9s14Td3ViSMUYz7OBzTlDLZpa8/edit?usp=sharing)
## PROBLEM DOMAIN
Write code to partition a linked list around a value X, such that all nodes less than X come before all nodes greater than or equal to X. If X is contained within the list, the value of X only needs to after the element less than X. The partition element X can appear anywhere in the "right partition", it does not need to appear between the left and right partitions.

## INPUT
13 -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> None
partition : 5

## OUTPUT
3 -> 1 -> 2 -> 10 -> 13 -> 5 -> 5 -> 8

## EDGE CASES
The partition can or not be in the LL.
I don't need to order the values of the LL.

## ALGORITHM

create a function that receives a LL head and a partition value.
add basic validations on the LL and partition
create a current node value and assign the value to the head
set a before node equals to none (so if I need to remove a node, knows how to maintain the link)
start traversing the ll while current.next is true
	if current value is equal or greater than X:
		set current node to a temp value
		# remove this node from that possition and append it to the end
		if before == none
			if current.next is not null, then I reassign the value of ll.head
				set the new ll.head to current.next
                  set before to current
		else
			set before.next equals to current.next

		set current.next equal to none, to break the link
	# create a helper function to append to LL the current node
	ll.append(current)
 	move current to temp.next
else
	move before to current
	move current to current.next


## TESTS
partition: 5
current: 13, 8
before: none, 13, 3, 5
temp:  13, 5, 8
head: 13, 3

input
     13 -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> None
     	            C^
               B^
               T^
          H^
output
13 -> none
5 -> none
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> -13 ->None
H^

## IDEAS TO IMPROVE
For the append function, I could have a variable on LL to point to the last node, so I don't have to traverse it all every time I need to append.

## BIG O
main function:
Time O(n): I need to traverse all the LL.
Space O(1): I'n not creating a new data structure here.

append function:
