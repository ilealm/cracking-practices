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


# My approach for this problem will the tackle in 3 parts: find the middle, reverse in place the second half of the LL,
# make the zip o both halfs in place
def reorder(head):
    # Step 1: obtain the middle
    middle_values = get_middle_node(head)
    # the middle value is not that acurate, BC I'm not traversing all the LL to be sure from all the nodes
    # to the right of the middle
    middle_node, middle_position, is_even = (
        middle_values[0],
        middle_values[1],
        middle_values[2],
    )

    # Step 2: reverse the 2nd half or the array
    reverse_half_linkedlist(head, middle_node, middle_position)

    # Step 3: make zip of the two helves
    node_left = head
    # in this point, my middle_node now is the last one, so I can't reference to it as the middle one,
    # I need to get get the new node at middle position
    node_right = get_k_node(head, middle_position)
    # print("the middle node is ", node_right.value)


    next_node_right = node_right.next
    while not next_node_right is None:
        next_node_left = node_left.next
        next_node_right = node_right.next

        node_left.next = node_right
        node_right.next = next_node_left

        # check here if == None, if so, I reached the final of the list so I need to to put a None at the end of the list
        if next_node_right == None:
            node_right.next = None
            break

        # move pointers for the next loop
        node_left = next_node_left
        node_right = next_node_right


# ------------ working
    # node_left = head
    # # in this point, my middle_node now is the last one, so I can't reference to it as the middle one,
    # # I need to get get the new node at middle position
    # node_right = get_k_node(head, middle_position)
    # # print("the middle node is ", node_right.value)

    # next_node_right = node_right.next
    # while not next_node_right is None:
    # # i = 1
    # # while i <= middle_position:
    #     next_node_left = node_left.next
    #     next_node_right = node_right.next

    #     # made the zip
    #     node_left.next = node_right
    #     node_right.next = next_node_left

    #     # check here if == None, if so, I reached the final of the list so I need to to put a None at the end of the list
    #     if next_node_right == None:
    #         node_right.next = None
    #         break

    #     # check if I reached the end of the Left side FOR AN ODD LL, which means I need to add the last node of the LL
    #     if not next_node_left.next == None and next_node_right.next == None:
    #         node_right.next = next_node_right
    #         next_node_right.next = None
    #         break

    #     # move pointer nodes to the next position
    #     node_left = next_node_left
    #     node_right = next_node_right



    print(head.print_list())
    print('here')


def main():
    # head = Node(2)
    # head.next = Node(4)
    # head.next.next = Node(6)
    # head.next.next.next = Node(8)
    # head.next.next.next.next = Node(10)
    # head.next.next.next.next.next = Node(12)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    # head = Node(2)
    # head.next = Node(4)
    # head.next.next = Node(6)
    # head.next.next.next = Node(8)
    # head.next.next.next.next = Node(10)

    # head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)
    # head.next.next.next.next = Node(50)

    # head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)

    # head = Node(2)
    # head.next = Node(4)
    # head.next.next = Node(6)
    # head.next.next.next = Node(8)
    # head.next.next.next.next = Node(10)
    # head.next.next.next.next.next = Node(12)

    reorder(head)
    # set the head to the new node
    # head = reverse_linkedlist(head)
    # print("in main....")
    head.print_list()
    # print("here")


main()



# -----

# original
#    # Step 3: make zip of the two helves
#     node_left = head
#     # in this point, my middle_node now is the last one, so I can't reference to it as the middle one,
#     # I need to get get the new node at middle position
#     node_right = get_k_node(head, middle_position)
#     # print("the middle node is ", node_right.value)


#     next_node_right = node_right.next
#     while not next_node_right is None:
#         next_node_left = node_left.next
#         next_node_right = node_right.next

#         node_left.next = node_right
#         node_right.next = next_node_left

#         # check here if == None, if so, I reached the final of the list so I need to to put a None at the end of the list
#         if next_node_right == None:
#             node_right.next = None
#             break

#         # move pointers for the next loop
#         node_left = next_node_left
#         node_right = next_node_right
