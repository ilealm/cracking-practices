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
        else:
            self.rear.after = new_node

        new_node.before = self.rear

        self.rear = new_node

        self.increase_items()

    def deqeue(self):
        if self.is_empty():
            raise Exception("The queue is empty.")

        value = self.front.value

        self.front = self.front.after

        self.decrease_items()

        return value

    def increase_items(self):
        self.items += 1

    def decrease_items(self):
        self.items -= 1

    def print_queue_from_rear(self):
        current = self.rear
        double_ll_values = "Double LL from Back => "
        while current:
            double_ll_values += "[ " + str(current.value) + " ]"
            # print(current.value)
            current = current.before

        return double_ll_values

    def print_queue_from_front(self):
        current = self.front
        double_ll_values = "Double LL from Front => "
        while current:
            # print(current.value)
            double_ll_values += "[ " + str(current.value) + " ]"
            current = current.after

        return double_ll_values


# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# # print(q.peek())
# # print(q.print_queue_from_rear())
# # print(q.print_queue_from_front())
# # me quede en hacer double link and dequeue
# print("deqeue: ", q.deqeue())
# print(q.print_queue_from_front())

# print("deqeue: ", q.deqeue())
# print(q.print_queue_from_front())
# q.enqueue(40)


# # print("deqeue: ", q.deqeue())
# print(q.print_queue_from_front())

# print("deqeue: ", q.deqeue())
# print(q.print_queue_from_front())

# print("deqeue: ", q.deqeue())
# print("deqeue: ", q.deqeue())
