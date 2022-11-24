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

    def _check_for_bubble_down(self):
        # validate if array only has 1 element
        if self.get_last_index() > 0:
            parent_index = 0
            self.array[parent_index] = self.array.pop()
            while self._need_to_bubble_down(parent_index):
                parent_index = self._do_bubble_down(parent_index)
        else:
            self.array.clear()

    def remove(self):
        if self.is_array_empty():
            return -1

        root = self.get_root()
        self._check_for_bubble_down()

        return root

    def print_heap(self):
        print(self.__str__())

    def testing(self):
        # other example
        heap_max = HeapMax()
        heap_max.add(15)
        heap_max.add(10)
        heap_max.add(3)
        heap_max.add(8)
        heap_max.add(12)
        heap_max.add(9)
        heap_max.add(4)
        heap_max.add(1)
        heap_max.add(24)
        heap_max.print_heap()
        print("\n\n")

        heap_max = HeapMax()
        heap_max.add(15)
        heap_max.add(10)
        heap_max.add(9)
        heap_max.add(8)
        heap_max.add(5)
        heap_max.add(3)
        heap_max.add(4)
        heap_max.print_heap()
        print("heap removed: ", heap_max.remove())
        print("heap removed: ", heap_max.remove())
        print("heap removed: ", heap_max.remove())
        print("heap removed: ", heap_max.remove())
        print("heap removed: ", heap_max.remove())
        print("heap removed: ", heap_max.remove())
        print("heap removed: ", heap_max.remove())
        print("heap removed: ", heap_max.remove())
        print("\n\n")

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
        print("\n\n")


class PriorityQueueWithHeap(HeapMax):
    def __init__(self):
        self._heap = HeapMax()

    def add(self, value):
        self._heap.add(value)

    def remove(self):
        return self._heap.remove()

    def print_priority_queue(self):
        self._heap.print_heap()

    def testing(self):
        prio_queueue = PriorityQueueWithHeap()
        prio_queueue.add(10)
        prio_queueue.add(5)
        prio_queueue.add(17)
        prio_queueue.add(4)
        prio_queueue.add(22)
        prio_queueue.print_priority_queue()
        prio_queueue.remove()
        prio_queueue.print_priority_queue()


class Heapify:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return str(self.array)

    def _get_array_size(self):
        return len(self.array) - 1

    def print_heapify(self):
        print(self.__str__())

    def _get_left_child_index(self, parent_index):
        return (parent_index * 2) + 1

    def _get_right_children_index(self, parent_index):
        return (parent_index * 2) + 2

    def _has_two_children(self, parent_index):
        return (
            self._get_right_children_index(parent_index)
            and self._get_left_child_index(parent_index)
        ) < self._get_array_size()

    def get_index_bigger_sibling(self, parent_index):
        left_children_index = self._get_left_child_index(parent_index)
        right_children_index = self._get_right_children_index(parent_index)

        if self._is_valid_index(left_children_index) and self._is_valid_index(
            right_children_index
        ):
            if self.array[left_children_index] > self.array[right_children_index]:
                return left_children_index
            else:
                return right_children_index

        return left_children_index

    def _is_valid_index(self, index):
        return True if index <= self._get_array_size() else False

    def _has_children(self, parent_index):
        left_children_index = self._get_left_child_index(parent_index)
        right_children_index = self._get_right_children_index(parent_index)

        if self._is_valid_index(left_children_index) and self._is_valid_index(
            right_children_index
        ):
            return True

        if self._is_valid_index(left_children_index):
            return True

        return False

    def _bubble_down(self, parent_index, children_index):
        self.array[children_index], self.array[parent_index] = (
            self.array[parent_index],
            self.array[children_index],
        )

    def _process_parent(self, parent_index):
        while self._has_children(parent_index):
            bigger_child_index = self.get_index_bigger_sibling(parent_index)
            if self.array[parent_index] < self.array[bigger_child_index]:
                self._bubble_down(parent_index, bigger_child_index)
                parent_index = bigger_child_index
            else:
                break

    def heapify(self):
        for index in range(len(self.array)):
            self._process_parent(index)


if __name__ == "__main__":
    os.system("clear")

    # MAX HEAPS
    # heap = HeapMax()
    # heap.testing()

    # PriorityQueue
    # prio_queueue = PriorityQueueWithHeap()
    # prio_queueue.testing()

    # HEAPIFY
    heapify = Heapify([5, 3, 8, 4, 1, 2])
    heapify.print_heapify()
    heapify.heapify()
    heapify.print_heapify()
