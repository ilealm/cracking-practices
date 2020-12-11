# Rearrange a LinkedList
# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half
# of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has
# nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.


from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        values = ""
        while temp is not None:
            values += str(temp.value) + " "
            # print(str(temp.value) + " ", end="")
            temp = temp.next
        # print()
        print(values)
        return values


# helper function that will return the middle node of the singly LL,
#  with the position on the LL and a true/false flag depending on
# if the ll is even or not.
def get_middle_node(head):
    slower = faster = head
    middle = 1  # is one BS I already started at 1 in the head

    while faster and faster.next:
        faster = faster.next.next
        middle += 1
        slower = slower.next

    #  I will return the middle node, the middle position and if the list is even or not
    return [slower, middle, middle % 2 == 0]


def reverse_all_linkedlist(head):
    prev = None

    while head:
        moving = head
        next_ = moving.next
        moving.next = prev
        prev = moving
        head = next_

    # Finally, I need to set the head to this finally moved node
    head = moving

    return head


# helper function that returns the k node of a LL
def get_k_node(head, k):
    current_node = head
    i = 1

    while current_node and i < k:
        current_node = current_node.next
        i += 1

    return current_node


# This functions reverse only a part of a singly ll.
def reverse_half_linkedlist(head, start_node, start_position):

    prev = None
    # break the first half of the ll, so I can rejoin with the reversed half
    end_first_half = get_k_node(head, start_position - 1)
    end_first_half.next = None

    # reverse the second half
    while start_node:
        next_ = start_node.next
        start_node.next = None
        moving = start_node

        moving.next = prev
        prev = moving
        start_node = next_

    # join halves
    end_first_half.next = moving

    # return head


# helper function that receives a LL and breacking point, the node before the break will point to None and the breacking point
# node will be returned
def break_ll(head, break_position):
    prev = None
    current_node = head
    i = 1

    while current_node and i < break_position:
        prev = current_node
        current_node = current_node.next
        i += 1

    # Break the LL on the node before of current
    prev.next = None
    # Current is now the head of the new LL
    return current_node



def do_zip(head, break_position):
    node_left = head
    next_node_left = node_left.next

    # step 3.1: break the LL so the zip works on even or odd ll
    node_right = break_ll(head, break_position)
    next_node_right = node_right.next

    while next_node_left and not next_node_right is None:
        next_node_left = node_left.next
        next_node_right = node_right.next

        node_left.next = node_right
        # I need to check if next_node_left is truty BS can be the end for an ODD LL
        if next_node_left:
            node_right.next = next_node_left

        # move pointers for the next loop
        if next_node_left:   # I need to check if next_node_left is truty BS can be the end for an ODD LL
            node_left = next_node_left
        node_right = next_node_right



# My approach for this problem will the tackle in 3 parts: find the middle, reverse in place the second half of the LL,
# make the zip o both halfs in place
def reorder(head):
    # Step 1: obtain the middle
    middle_values = get_middle_node(head)
    # the middle value and is_even is not that acurate, BC I'm not traversing all the LL to be sure from all the nodes
    # to the right of the middle
    middle_node, middle_position, is_even = (
        middle_values[0],
        middle_values[1],
        middle_values[2],
    )

    # Step 2: reverse the 2nd half or the array
    reverse_half_linkedlist(head, middle_node, middle_position)

    # Step 3: make zip of the two helves
    do_zip(head, middle_position)

