# LinkedList Cycle
# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# faster HAVE TO move 2 positions ahead in order to not be cycled in a loop in the LL, if there is a cycled loop
def has_cycle(head):
    slower = head
    faster = head.next.next

    while faster:
        if faster == slower:
            # I found the cycle, so I need to exit
            return True

        slower = slower.next
        faster = faster.next.next


    return False



def has_cycle_v0(head):
    # stablish my pointers
    slower = head
    faster = slower.next.next

    while slower.next:
        # my faster will check if there is a .next that points to slower, if so, return True
        # if faster.next == slower:
        if faster == slower:
            return True

        slower = slower.next
        # I need to validate how much I can move my faster in case there is no loop.
        if faster.next:
            if faster.next.next:
                faster = faster.next.next
            else:
                faster = faster.next


    return False



