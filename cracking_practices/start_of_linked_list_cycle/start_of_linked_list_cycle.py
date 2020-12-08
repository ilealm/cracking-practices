# Start of LinkedList Cycle
# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next



def find_cycle_length(head):
    slower = head
    faster = head.next.next
    counter = 0
    start_couting = False

    while faster and faster.next:
        if slower == faster:
            if not start_couting:
                # reset the positions to start couting
                faster = slower
                start_couting = True
            else:
                # I reach the next loop, so return counter
                return counter

        if start_couting:
            counter += 1

        slower = slower.next
        faster = faster.next.next

    return counter


def find_cycle_start(head):
    slower = head
    faster = head
    # first, I need to get the length of the cycle
    k = find_cycle_length(head)

    # now, I will move faster k positions ahead
    for i in range(k):
        faster = faster.next

    # now, I will move both pointers 1 position until both are at the same place,
    # there is the start of the cycle
    while not slower == faster:
        slower = slower.next
        faster = faster.next


    return slower.value


