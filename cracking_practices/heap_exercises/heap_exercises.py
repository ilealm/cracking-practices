import os


class HeapMax:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def get_last_index(self):
        return len(self.array)-1

    def _get_parent_index(self, child_index):
        return int((child_index - 1) / 2)

    def _need_to_bubble_up(self, child_index):
        parent_index = self._get_parent_index(child_index)
        print("parent_index ", parent_index)

        if parent_index < 0 : return False

        return int(self.array[child_index]) > int(self.array[parent_index])

    def _bubble_up(self, parent_index, child_index):
        self.array[parent_index], self.array[child_index] =  self.array[child_index], self.array[parent_index]


    def add(self, value):
        self.array.append(value)
        current_index = self.get_last_index()

        while self._need_to_bubble_up(current_index):
            parent_index = self._get_parent_index(current_index)
            self._bubble_up(parent_index, current_index)
            current_index = parent_index


    def delete(self):
        pass


if __name__ == "__main__":
    os.system("clear")
    heap_max = HeapMax()
    heap_max.add(15)
    heap_max.add(10)
    heap_max.add(3)
    heap_max.add(8)
    heap_max.add(12)
    print(heap_max)
