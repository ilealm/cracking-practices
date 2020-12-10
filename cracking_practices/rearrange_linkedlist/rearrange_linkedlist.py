from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end="")
            temp = temp.next
        print()


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


def reversev1(head):
    main_head = head
    prev = None
    while head:
        moving = head
        head = head.next
        moving.next = prev
        prev = moving

    head = moving


def reverse(head):
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

    # head.print_list()


# My approach for this problem will the tackle in 3 parts: find the middle, reverse in place the second half of the LL,
# make the zip o both halfs in place
def reorder(head):
    # This problem
    # TODO: Write your code here
    middle_values = get_middle_node(head)
    # the middle value is not that acurate, BC I'm not traversing all the LL to be sure from all the nodes to the right of
    # the middle
    middle, position, is_even = middle_values[0], middle_values[1], middle_values[2]

    print("middle node: ", middle.value, "position: ", position)
    reverse(head)

    return


def main():
    # head = Node(2)
    # head.next = Node(4)
    # head.next.next = Node(6)
    # head.next.next.next = Node(8)
    # head.next.next.next.next = Node(10)
    # head.next.next.next.next.next = Node(12)
    # head.next.next.next.next.next.next = Node(120)

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # reorder(head)
    head = reverse(head)
    print("in main....")
    head.print_list()
    print('here')


main()
