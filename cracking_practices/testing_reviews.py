# # from __future__ import print_function


# # class Node:
# #   def __init__(self, value, next=None):
# #     self.value = value
# #     self.next = next

# #   def print_list(self):
# #     temp = self
# #     while temp is not None:
# #       print(str(temp.value) + " ", end='')
# #       temp = temp.next
# #     print()


# # def reorder(head):
# #   if head is None or head.next is None:
# #     return

# #   # find middle of the LinkedList
# #   slow, fast = head, head
# #   while fast is not None and fast.next is not None:
# #     slow = slow.next
# #     fast = fast.next.next

# #   # slow is now pointing to the middle node
# #   head_second_half = reverse(slow)  # reverse the second half
# #   head_first_half = head

# #   # rearrange to produce the LinkedList in the required order
# #   while head_first_half is not None and head_second_half is not None:
# #     temp = head_first_half.next
# #     head_first_half.next = head_second_half
# #     head_first_half = temp

# #     temp = head_second_half.next
# #     head_second_half.next = head_first_half
# #     head_second_half = temp

# #   # set the next of the last node to 'None'
# #   if head_first_half is not None:
# #     head_first_half.next = None


# # def reverse(head):
# #   prev = None
# #   while head is not None:
# #     next = head.next
# #     head.next = prev
# #     prev = head
# #     head = next
# #   return prev


# # def main():
# #   head = Node(2)
# #   head.next = Node(4)
# #   head.next.next = Node(6)
# #   head.next.next.next = Node(8)
# #   head.next.next.next.next = Node(10)
# #   head.next.next.next.next.next = Node(12)
# #   reorder(head)
# #   head.print_list()


# # main()


# # My approach for this problem will the tackle in 3 parts: find the middle, reverse in place the second half of the LL,
# # make the zip o both halfs in place
# def reorder(head):
#     # Step 1: obtain the middle
#     middle_values = get_middle_node(head)
#     # the middle value is not that acurate, BC I'm not traversing all the LL to be sure from all the nodes
#     # to the right of the middle
#     middle_node, middle_position, is_even = (
#         middle_values[0],
#         middle_values[1],
#         middle_values[2],
#     )

#     # Step 2: reverse the 2nd half or the array
#     # print("middle node: ", middle_node.value, "middle_position: ", middle_position)
#     reverse_half_linkedlist(head, middle_node, middle_position)

#     # Step 3: make zip of the two helves
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

#         # # validation for odd LL
#         # if next_node_right.next == None:
#         #     node_left = next_node_left
#         #     print("here")
#         #     node_right.next = next_node_right
#         #     break

#         # move pointers for the next loop
#         node_left = next_node_left
#         node_right = next_node_right

#     print(head.print_list())
#     print('here')


# Step 3: make zip of the two helves
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
