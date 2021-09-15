# [ Linked List Queue ](cracking_practices/linked_list_queue/README.md)
# - Build a queue using a linked list from scratch. Implement the following operations: enqueue, dequeue, peek, size and is_empty.


class Node:
    def __init__(self, value):
        self.value = value
        self.after = None
        self.before = None

    def __repr__(self) -> str:
        return f"{self.value} -> {self.before}"


class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.items = 0

    def __repr__(self) -> str:
        return f"{self.rear}"

    def is_empty(self):
        return self.items == 0

    def size(self):
        return self.items

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty.")

        return self.front.value


    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node

        new_node.before = self.rear
        # TODO create link to next from rear
        # self.rear.after = new_node
        self.rear = new_node

        self.items += 1




    def deqeue(self):
        if self.is_empty():
            raise Exception("The queue is empty.")

        value = self.front.value

        print(self.front.after.value)
        # me quede intentando quitar el link de front
        self.front = self.front.before
        return value


    def print_queue(self):
        current = self.rear
        print('Back...')
        while current:
            print(current.value)
            current = current.before


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
# print(q.peek())
print(q.print_queue())
# me quede en hacer double link and dequeue
# print(q.deqeue())
# print(q)

