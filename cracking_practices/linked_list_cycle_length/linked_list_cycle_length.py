# Length of the Cycle in LL
# Given the head of a LinkedList with a cycle, find the length of the cycle.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_length(head):
    slower = head
    faster = head.next.next
    counter = 0
    start_counting = False

    while faster and faster.next:
        # I found the lopp, so I will start counting
        if faster == slower:
            if counter == 0:
                # I'm going to start counting, so reset the position of faster.
                # so reset the position of faster to 2x from slower (this will be my start point)
                faster = slower
                start_counting = True
            else:
                # I finished counting the second loop, so return the count and exit the cycle
                return counter

        if start_counting:
            counter += 1

        slower = slower.next
        faster = faster.next.next

    return counter


