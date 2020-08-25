# PROBLEM DOMAIN
# Return Ordered List
# Having a list of thousands of unordered numbers from 1 - 100, return an ordered list with all these values in order.


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# -------
# ------- APPROACH 1, implementing linked list
# -------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
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

# Approach 1, Implement a LL
# Implement a link list (ll) to save on ordering fashion the values, and each node will have a counter of the occurrence of that number. At the end traverse the ll and return a list.
# Pros: traversing the LL to find values will be faster
# Cons: I will create a new DD to store in worst-case scenario 100 nodes. and then create a new list to return the values in order way.
def return_ordered_list(unordered_list):
    ll_ordered = LinkedList()
    return_ordered_list = []
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
                break

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
            else:
                #  I'm at some point in the ll, check if I need to insert here.
                if current.next.value > unordered_list[i]:
                    new_node.next = current.next
                    current.next = new_node
                    break


            previous = current
            current = current.next


    # convert the ll to a list whit the exact ocurrences of each number
    current = ll_ordered.head

    while current:
        for i in range(0, current.counter):
            return_ordered_list.append(current.value)

        current = current.next

    return(return_ordered_list)


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# -------
# ------- APPROACH 2, implementing trees
# -------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
from collections import deque

class NodeTree:
    def __init__(self, value, left = None,  rigth = None):
        self.value = value
        self.counter = 1
        self.left = left
        self.right = rigth

    def __str__(self):
        return f"Node: {self.value}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if not self.root : return 'The root is empty.'

        return f'The root is {self.root.value}'


    def preOrder(self):
        list_return = []

        if self.root == None : return list_return

        def traverse(current_node):
            if not current_node : return

            list_return.append(current_node.value)
            traverse(current_node.left)
            traverse(current_node.right)

        traverse(self.root)

        return list_return

    def inOrder(self):
        list_return = []

        if self.root == None : return list_return

        def traverse(current_node):
            if not current_node : return

            traverse(current_node.left)
            for i in range(0, current_node.counter):
                list_return.append(current_node.value)

            traverse(current_node.right)


        traverse(self.root)
        return list_return

class BinarySearchTree(BinaryTree):
    def __str__(self):
        if not self.root : return 'The root is empty.'

        return f'The root is {self.root.value}'


    def add(self, value):
        new_node = NodeTree(value)

        if self.root == None :
            self.root = new_node
            return

        def traverse(current_node, new_node):

            if not current_node : return

            if current_node.value == new_node.value:
                current_node.counter += 1
                return

            if new_node.value < current_node.value:
                if current_node.left == None :
                    current_node.left = new_node
                else:
                    traverse(current_node.left, new_node)
            else:
                if current_node.right == None :
                    current_node.right = new_node
                else:
                    traverse(current_node.right, new_node)

        traverse(self.root, new_node)



def return_ordered_list_using_BST(unordered_list):
    bst = BinarySearchTree()
    for i in range(0, len(unordered_list)):
        bst.add(unordered_list[i])

    return bst.inOrder()


if __name__ == "__main__":



    unordered_list = [30,30,50,70,50,35,35,35,35,90,10, 22,30,1,1,1,1,1,100]
    # unordered_list = [50, 30, 10,10, 80, 35,70,80]
    print(unordered_list)

    print(return_ordered_list_using_BST(unordered_list))

