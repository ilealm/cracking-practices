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
        # I start in 1 BC I assume [0] is at correct possition
        for i in range(1, len(self.array)):
            current = self.array[i]
            j = i - 1
            # while j is bigger than current, I will keep shifting values
            while j >= 0 and self.array[j] > current:
                self.array[j + 1] = self.array[j]
                j = j - 1
            # It needs to be [j+1] BC in the while, I decrement it, and if I don't enter there,
            # I need to put it in the same space that it was
            self.array[j + 1] = current

        return self.array


class MergeSort:
    def merge(self, left_array, right_array):
        merged = []
        l_pointer = r_pointer = 0

        while l_pointer < len(left_array) and r_pointer < len(right_array):
            if left_array[l_pointer] < right_array[r_pointer]:
                merged.append(left_array[l_pointer])
                l_pointer += 1
            else:
                merged.append(right_array[r_pointer])
                r_pointer += 1

        # append all what was left in the array, after the pointers
        merged += left_array[l_pointer:]
        merged += right_array[r_pointer:]

        return merged

    def sort(self, array):
        if array == []:
            return array

        def traverse(array):
            if len(array) == 1:
                return array

            half = len(array) // 2
            left = array[0:half]
            right = array[half:]

            sorted_left = traverse(left)
            sorted_right = traverse(right)

            return self.merge(sorted_left, sorted_right)

        return traverse(array)


class QuickSort:
    # returns the index of the pivot atfer it moved to the rigth possition
    # the pivot will be the last item on the array
    def partition(self, array, start, end):
        pivot = array[end]
        smaller_elements_index = start - 1

        for i in range(start, end):
            if array[i] < pivot:
                smaller_elements_index += 1
                array[i], array[smaller_elements_index] = (
                    array[smaller_elements_index],
                    array[i],
                )

        # This ensures that the pivot is now in its correct position
        array[smaller_elements_index + 1], array[end] = (
            array[end],
            array[smaller_elements_index + 1],
        )
        return smaller_elements_index + 1

    def sort(self, array):
        def sort_recursion(array, start, end):
            if start >= end:
                return

            # partition
            boundary = self.partition(array, start, end)
            # left
            sort_recursion(array, start, boundary - 1)
            # right
            sort_recursion(array, boundary + 1, end)

        sort_recursion(array, 0, len(array) - 1)

        return array


if __name__ == "__main__":
    import os

    os.system("clear")
    sort = QuickSort()

    # # array = [8,2,4,7,1,3,9,6,5]
    array = [15, 6, 3, 1, 22, 10, 13]
    # print(array)
    print(sort.sort(array))

# from heapq import nlargest

# heap = [1, 5, 3, 2, 4]
# k=3

# largest_values = nlargest(k, heap)

# print(largest_values)
