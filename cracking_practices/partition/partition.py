# PROBLEM DOMAIN
# Write code to partition a linked list around a value X, such that all nodes less than X come before all nodes greater than or equal to X.
# If X is contained within the list, the value of X only needs to after the element less than X. The partition element X can appear anywhere in
# the "right partition", it does not need to appear between the left and right partitions.

from cracking_practices.linked_list.linked_list import LinkedList, Node

# at root, execute: PYTHONPATH='.' python cracking_practices/partition/partition.py

# WORKING SOLUTION
# Approach 1
# I'm going to obtain traverse all the ll, if the current node.value >= partition, I will remove it and appending to the same ll,
# without losing the link of the nodes before. If I need to append, I will get the tail only once, and updating it on each append.
# Also, I'm using a pointer to the first appended node, so I don't re visit them
def partition(ll, partition):
    if not ll.head:
        raise Exception('The linked list is empty.')

    before = None
    current = ll.head
    ll_tail = None # I'm going to traverse all the ll only if I have to. This to have better performance.
    pointer_appened = None # to know when I have to stop the traverse in the while, so I don't re visit appended nodes
    while current:
        if current == pointer_appened:
            break # so I don't revisit appended nodes
        if current.value >= partition:
            # if I'm here, I will need to traverse the ll once to get the tail of ll, so I can append
            if not ll_tail:
                ll_tail = get_ll_tail(ll) # I'm going to get ot only once

            # unlink from the ll and re linkit to the end of the ll
            after = current.next
            if before:
                before.next = after
            else:
                ll.head = after
            current.next = None

            if not pointer_appened:
                pointer_appened = current
            ll_tail.next = current
            ll_tail = current
        else:
            before = current
            after = current.next

        current = after # move to the next node

    return ll

# Returns the last node of the given ll
def get_ll_tail(ll):
    current = ll.head
    while current.next:
        current = current.next

    return current


# WORKING SOLUTION
# Approach 2
# This is the simplest solution. It traverse the original ll and for each value, it appends / insert
# in a new list, and returns that new list.
# Big O: Time O(n), we are traversing all the list. Space O(n): We are creating a copy of the LL
def partition_new_ll(ll, partition):
    if not ll.head:
        raise Exception('The linked list is empty.')

    return_ll = LinkedList()

    current = ll.head
    while current:
        if current.value >= partition:
            return_ll.append(current.value)
        else:
            return_ll.insert(current.value)

        current = current.next

    return return_ll

    

# WORKING SOLUTION
# Approach 3
# This approach traverse the ll and check if current.value >= partition, if so, this node
# is removed from the ll and put in a temporaly list (which only refers the node, so no new ds is created)
# and at the end of the traverse, the temp list is appended to the end of the list.
# With this approach we asure we only traverse the original list once, and not re traverse nodes that had
# already visited. I like this approach the most
def partition_append_just_greater_or_equals(ll, partition):
    if not ll.head:
        raise Exception('The linked list is empty.')

    current = ll.head
    temp_ll_head = None
    before = None
    while current:
        after = current.next
        if current.value >= partition:
            # before unlink, I need to save whatever I have before in the ll
            if not before == None:
                before.next = current.next
            # unlink this node to the original ll
            if current == ll.head:
                ll.head = current.next
            if before == None:
                ll.head = after
            current.next = None
            # link this node to the temp_ll
            if temp_ll_head == None:
                temp_ll_head = current
            else:
                current.next = temp_ll_head
                temp_ll_head = current
        else:
            before = current

        current = after

    # current is already at the end of the ll, so I will add the temp ll to current.next
    before.next = temp_ll_head

    return ll

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.insert(1)
#     ll.insert(2)
#     ll.insert(10)
#     ll.insert(5)
#     ll.insert(8)
#     ll.insert(5)
#     ll.insert(3)
#     ll.insert(13)
#     ll.insert(0)

#     print('original', ll)
#     print('updated partition', partition(ll, 5))
    # print('updated', partition_new_ll(ll, 5))
    # print('updated: partition_append_just_greater_or_equals', partition_append_just_greater_or_equals(ll, 5))



