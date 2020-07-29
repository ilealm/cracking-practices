# PROBLEM DOMAIN
# Write code to partition a linked list around a value X, such that all nodes less than X come before all nodes greater than or equal to X.
# If X is contained within the list, the value of X only needs to after the element less than X. The partition element X can appear anywhere in
# the "right partition", it does not need to appear between the left and right partitions.

# from cracking_practices.linked_list.linked_list import LinkedList, Node

# in root, execute: PYTHONPATH='.' python cracking_practices/partition/partition.py

# Approach 1
def partition(ll, partition):
    if not ll.head:
        raise Exception('The linked list is empty.')

    before = None
    current = ll.head
    while current:
        if current.value >= partition:
            # I need to move the node to the end of the ll
            # temp_node = current
            # remove this node from that possition and append it to the end
            if before == None:
                if not current.next == None:
                    ll.head = current.next
                # before = current
            # else:
            #     before = current
            # break the link of the node that will be appended
            temp_node = current.next
            current.next = None
            ll.append(current.value)
            current = temp_node
        else:
            before = current
            current = current.next

        # problem: i need to also move the values than are less
        # if not before == None:
        #     if current.value > before.value:
        #         current.value, before.value =  before.value, current.value

    return(ll)


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
# already visited.
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
            # if before == None, set this as the new before
        else:
            before = current

        current = after

    # current is already at the end of the ll, so I will add the temp ll to current.next
    before.next = temp_ll_head

    return ll


# start delete
class Node():
    def __init__ (self, value, next_ = None):
        self.value =  value
        self.next = next_

        if (not next_ == None) and ( not isinstance(next_, Node)):
            raise TypeError("The value of the next node MUST be a node")


    def __repr__(self):
        return f"{self.value} -> {self.next}"


class LinkedList():
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"The head is {self.head}"

    def insert(self, value):
        new_node = Node(value)
        if self.head : new_node.next = self.head
        self.head = new_node

    def append(self,value):
        new_node = Node(value)
        current = self.head

        # if the head is none, then call insert function
        if not current :
            self.insert(value)
            return

        while current.next:
            current = current.next
        current.next = new_node



# end delete
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(10)
    ll.insert(5)
    ll.insert(8)
    ll.insert(5)
    ll.insert(3)
    ll.insert(13)

    print('original', ll)
    # print('updated', partition(ll, 5))
    # print('updated', partition_new_ll(ll, 5))
    print('updated: partition_append_just_greater_or_equals', partition_append_just_greater_or_equals(ll, 5))



