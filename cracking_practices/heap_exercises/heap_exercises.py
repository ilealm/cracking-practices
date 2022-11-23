import os


class HeapMax:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def get_last_index(self):
        return len(self.array) - 1

    def _get_parent_index(self, child_index):
        return int((child_index - 1) / 2)

    def _need_to_bubble_up(self, child_index):
        parent_index = self._get_parent_index(child_index)

        if parent_index < 0:
            return False

        return int(self.array[child_index]) > int(self.array[parent_index])

    def _bubble_up(self, parent_index, child_index):
        self.array[parent_index], self.array[child_index] = (
            self.array[child_index],
            self.array[parent_index],
        )

    def add(self, value):
        self.array.append(value)
        current_index = self.get_last_index()

        while self._need_to_bubble_up(current_index):
            parent_index = self._get_parent_index(current_index)
            self._bubble_up(parent_index, current_index)
            current_index = parent_index

    def get_root(self):
        if self.is_array_empty():
            return -1

        return self.array[0]

    def is_array_empty(self):
        return len(self.array) == 0

    def _get_left_children_index(self, parent_index):
        return (parent_index * 2) + 1

    def _get_right_children_index(self, parent_index):
        return (parent_index * 2) + 2

    def parent_has_two_children(self, left_childen_index, right_childen_index):
        return (left_childen_index and right_childen_index) <= self.get_last_index()

    def get_index_bigger_sibling(self, left_childen_index, right_childen_index):
        return (
            left_childen_index
            if (self.array[left_childen_index] > self.array[right_childen_index])
            else right_childen_index
        )

    def _bubble_down(self, parent_index, child_index):
        self.array[parent_index], self.array[child_index] = (
            self.array[child_index],
            self.array[parent_index],
        )

    def _do_bubble_down(self, parent_index):
        left_childen_index = self._get_left_children_index(parent_index)
        right_childen_index = self._get_right_children_index(parent_index)

        if self.parent_has_two_children(left_childen_index, right_childen_index):
            bigger_index = self.get_index_bigger_sibling(
                left_childen_index, right_childen_index
            )
            self._bubble_down(parent_index, bigger_index)

            return bigger_index
        else:
            if left_childen_index <= self.get_last_index():
                if self.array[parent_index] < self.array[left_childen_index]:
                    self._bubble_down(parent_index, left_childen_index)
                    return parent_index

    def _need_to_bubble_down(self, parent_index):
        left_childen_index = self._get_left_children_index(parent_index)
        right_childen_index = self._get_right_children_index(parent_index)

        if self.parent_has_two_children(left_childen_index, right_childen_index):
            greater = max(
                self.array[left_childen_index], self.array[left_childen_index]
            )
            if greater > self.array[parent_index]:
                return True
        else:
            if left_childen_index <= self.get_last_index():
                if self.array[parent_index] < self.array[left_childen_index]:
                    return True

        return False

    def remove(self):
        if self.is_array_empty():
            return -1

        root = self.get_root()

        # validate if array only has 1 element
        if self.get_last_index() > 0:
            parent_index = 0
            self.array[parent_index] = self.array.pop()
            while self._need_to_bubble_down(parent_index):
                parent_index = self._do_bubble_down(parent_index)
        else:
            self.array.clear()

        return root

    def print_heap(self):
        print(self.__str__())


if __name__ == "__main__":
    os.system("clear")
    heap_max = HeapMax()
    # mosh example
    # heap_max.add(15)
    # heap_max.add(10)
    # heap_max.add(3)
    # heap_max.add(8)
    # heap_max.add(12)
    # heap_max.add(9)
    # heap_max.add(4)
    # heap_max.add(1)
    # heap_max.add(24)

    # delete example
    heap_max.add(15)
    heap_max.add(10)
    heap_max.add(9)
    heap_max.add(8)
    heap_max.add(5)
    heap_max.add(3)
    heap_max.add(4)
    heap_max.print_heap()
    # print("original")
    # print(heap_max)
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())

    print("\n\n")

    # mosh example
    heap_max = HeapMax()
    heap_max.add(10)
    heap_max.add(5)
    heap_max.add(17)
    heap_max.add(4)
    heap_max.add(22)
    heap_max.print_heap()
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    print("heap removed: ", heap_max.remove())
    heap_max.print_heap()
