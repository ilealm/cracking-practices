# PROBLEM DOMAIN
# Return Ordered List
# Having a list of thousands of unordered numbers from 1 - 100, return an ordered list with all these values in order.


class Node():
    def __init__ (self, value, next_ = None):
        self.value =  value
        self.counter = 1
        self.next = next_

        if (not next_ == None) and ( not isinstance(next_, Node)):
            raise TypeError("The value of the next node MUST be a node")


    def __repr__(self):
        return f"{self.value}, # {self.counter} -> {self.next}"


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


def return_ordered_list(unordered_list):
    ll_ordered = LinkedList()
    list_ordered = []
    previous = None
    current = ll_ordered.head

    for i in range(0, len(unordered_list)):
        # case when the ll is empty, so insert list[0] as the head
        if not ll_ordered.head:
            new_node = ll_ordered.insert(unordered_list[i])
            continue  # ends cicle at this point and return to the for loop

        # start traversing the ll to find the right spot to insert / update the LL
        current = ll_ordered.head
        while current:
            if current.value == unordered_list[i]:
                current.counter += 1
                break  # this works fine

            new_node = Node(unordered_list[i])

            # case when I need to intert in the top (head) of the list
            if current.value > unordered_list[i]:
                new_node.next = current
                ll_ordered.head = new_node
                break

            # peek in current.next
            # case when I'm at the end of the ll
            if not current.next:
                if current.value < unordered_list[i]:
                    current.next = new_node
                else:
                    # i need to reasign the previuos pointer to new node, and new node to current
                    previous.next = new_node
                    new_node.next = current
                break
                # continue
            else:
                #  I'm at some point in the ll, check if I need to insert here.
                if current.next.value > unordered_list[i]:
                    new_node.next = current.next
                    current.next = new_node
                    break
                    # continue


            previous = current
            current = current.next

    return(ll_ordered)


# 		set previous to current
# 		set current to current.next






if __name__ == "__main__":



    unordered_list = [30,30,50,70,50,35,35,35,35,90,10, 22,30,1,1,1,1,1,100]
    # unordered_list = [30,50,10]
    print(unordered_list)

    print(return_ordered_list(unordered_list))
