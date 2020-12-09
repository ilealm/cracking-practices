# Palindrome LinkedList (medium) #
# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the original form once
# the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true

# Example 2:
# Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
# Output: false


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


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


# helper function that returns the k node of a LL
def get_k_node(head, k):
    current_node = head
    i = 1

    while current_node and i < k:
        current_node = current_node.next
        i += 1

    return current_node


# My approach is to get the middle of the LL, and from there, i will have 2 pointers: left and right, and I will compare each other moving
# towards the outer limits
def is_palindromic_linked_list(head):
    middle_info = get_middle_node(head)
    middle_node, middle_position, is_even = (
        middle_info[0],
        middle_info[1],
        middle_info[2],
    )

    # set my pointers to start the comparing, from the middle to the edges
    left_position = middle_position - 1
    pointer_left = get_k_node(head, left_position)
    # depending on if is even or not the LL, i will possition the pointers left and rigth to check against each other
    if is_even:
        pointer_right = middle_node
    else:
        pointer_right = middle_node.next


    while pointer_right:
        if not pointer_left.value == pointer_right.value:
            return False

        left_position -= 1
        pointer_left = get_k_node(head, left_position)
        pointer_right = pointer_right.next

    return True
