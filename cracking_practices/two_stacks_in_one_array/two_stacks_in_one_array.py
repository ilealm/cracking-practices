# Implement two stacks in one array.
# Support these operations:
# push1() // to push in the first stack
# push2() // to push in the second stack
# pop1()
# pop2()
# isEmpty1()
# isEmpty2()
# isFull1()
# isFull2()
# Make sure your implementation is space efficient. (hint: do not allocate the same amount of space by dividing the array in half.)


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

        # I will not reasing a new value to the poped position, is pointless
        self.left_pointer -= 1
        return self.stack[self.left_pointer ]


    # Operations to the right of the array (2)
    def push2(self, value):
        if self.is_stack_full(): raise NameError('The stack is full.')
        self.stack[self.right_pointer] = value

        self.right_pointer -= 1


    def pop2(self):
        if self.right_pointer == self.array_lenght-1 : raise NameError('The stack is empty.')

        # I will not reasing a new value to the poped position, is pointless
        self.right_pointer += 1
        return self.stack[self.right_pointer]


    # helper functions
    def is_stack_full(self):
        if self.left_pointer == self.right_pointer :
            return self.left_pointer == self.right_pointer

        # the stack is full from the left
        if self.left_pointer == self.array_lenght - 1 :
            return True

        # the stack is full from the right
        if self.right_pointer == 0:
            return True

        return False

