class Stack:
    def __init__(self):
        self.array_lenght = 10
        self.left_pointer = 0
        self.right_pointer = self.array_lenght - 1
        self.stack = [None] * self.array_lenght

    def get_stack_lenght(self):
        return len(self.array_stack)

    # Operations to the left side of the array (1)
    def push1(self, value):
        if self.is_stack_full():
            raise NameError("The stack is full.")

        # add the item to the left of the array
        self.stack[self.left_pointer] = value
        self.left_pointer += 1

    def pop1(self):
        if self.left_pointer == 0:
            raise NameError('The stack is empty.')

        self.left_pointer -= 1
        return self.stack[self.left_pointer ]


    # Operations to the right of the array (2)
    def push2(self, value):
        return "TDB"

    def pop2(self):
        return "TDB"

    # helper functions
    def is_stack_full(self):
        return self.left_pointer == self.right_pointer


my_stack = Stack()
my_stack.push1("a")
my_stack.push1("b")
my_stack.push1("c")
print(my_stack.stack)
print(my_stack.pop1())
print(my_stack.pop1())
print(my_stack.pop1())
my_stack.push1("A")
my_stack.push1("B")
print(my_stack.stack)
print(my_stack.pop1())
