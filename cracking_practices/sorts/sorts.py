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

        # I want to decrease the outer loop so I don't pass numbers that are in its right order
        for outer in range((len(self.array) - 1), 0, -1):
            # if I didn't do any swaping, means the array is already sorted and I don't need to keep looking
            is_sorted = True
            for p in range(self.get_num_items() - 1):
                if self.array[p] > self.array[p + 1]:
                    self.swap(p, p + 1)
                    is_sorted = False

            if is_sorted:
                return self.array

        return self.array


# sdf
if __name__ == "__main__":
    import os

    os.system("clear")
    sort = BubbleSort([9, 1, 50, 1, 7])
    print(sort)
    sort.sort()
    print(sort)
