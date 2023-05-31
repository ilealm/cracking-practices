from typing import Any


class BubbleSort:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return f"{self.array}"

    def __repl__(self):
        return f"{self.array}"

    def is_empty(self):
        return len(self.array) == 0

    def get_num_items(self):
        return len(self.array)

    def swap(self, left, right):
        self.array[left], self.array[right] = self.array[right], self.array[left]

    def sort(self):
        if self.is_empty():
            return []

        num_items = self.get_num_items() - 1
        # I want to decrease the outer loop so I don't pass numbers that are in its right order
        for outer in range((num_items), 0, -1):
            # if I didn't do any swaping, means the array is already sorted and I don't need to keep looking
            is_sorted = True
            for p in range(num_items):
                if self.array[p] > self.array[p + 1]:
                    self.swap(p, p + 1)
                    is_sorted = False

            if is_sorted:
                return self.array

        return self.array


class SelectionSort:
    def __init__(self, array):
        self.array = array
        self.num_items = len(array)

    def __str__(self):
        return f"{self.array}"

    def swap(self, left, right):
        self.array[left], self.array[right] = self.array[right], self.array[left]

    def sort(self):
        if self.num_items == 0:
            return []

        items = self.num_items

        for p in range(items):
            # in each iteration, I need to reset the values to the unsorted ones.
            min_index = p
            for inner in range(p + 1, items):
                if self.array[inner] < self.array[min_index]:
                    min_index = inner
            self.swap(p, min_index)

        return self.array


class InsertionSort:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return f"{self.array}"

    
    def sort(self):
        for i in range(1, len(self.array)):
            current = self.array[i]
            j = i-1
            while j >= 0 and self.array[j] > current:
                self.array[j+1] = self.array[j]
                j = j -1

            self.array[j+1] = current

        return self.array



if __name__ == "__main__":
    import os

    os.system("clear")
    sort = InsertionSort([8, 2, 4, 1, 3])
    print(sort)
    sort.sort()
    print(sort)
