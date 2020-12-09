# Middle of the LinkedList
# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
# If the total number of nodes in the LinkedList is even, return the second middle node.



class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


# I will use approach of 2 pointers: slower and faster. Faster will move 2x and will be the one I will be moving
def find_middle_of_linked_list(head):
    slower = head
    faster = head

    while faster and faster.next:
        faster = faster.next.next
        slower = slower.next

    return slower.value


