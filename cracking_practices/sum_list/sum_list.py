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

# PROBLEM DOMAIN, 4.5, SUM LIST
# You have 2 numbers represented by 2 linked list, where each node contains a single digit. The digits are stored in reverse order,
# such that the 1st digit is at the head of the list. White a function that adds the 2 numbers and returns the sum as a linked list.

# function that traverse the ll and return a string containig all the values in reverse order and as a string.
def get_ll_values_in_reverse(linked_list):
    current = linked_list.head
    ll_values = ''
    while current:
        ll_values = str(current.value) + ll_values
        current = current.next

    return ll_values


def sum_list(first_ll, second_ll):
    return_ll = LinkedList()
    if not first_ll:
        raise Exception('The first list is not valid')
        return
    if not first_ll:
        raise Exception('The second list is not valid')
        return

    first_ll_value = get_ll_values_in_reverse(first_ll)
    second_ll_value = get_ll_values_in_reverse(second_ll)

    ll_sum = str(int(first_ll_value) + int(second_ll_value))

    for ch in ll_sum:
        return_ll.insert(ch)

    return return_ll


# if __name__ == "__main__":
#     first_ll = LinkedList()
#     first_ll.insert(6)
#     first_ll.insert(1)
#     first_ll.insert(7)
#     second_ll = LinkedList()
#     second_ll.insert(2)
#     second_ll.insert(9)
#     second_ll.insert(5)

#     print(first_ll)
#     print(second_ll)

#     print(sum_list(first_ll, second_ll))
