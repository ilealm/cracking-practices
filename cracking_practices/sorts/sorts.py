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
            for p in range(self.get_num_items() - 1):
                if self.array[p] > self.array[p + 1]:
                    self.swap(p, p + 1)

        return self.array


# sdf
if __name__ == "__main__":
    import os

    os.system("clear")
    sort = BubbleSort([8, 2, 4, 1, 3, 6, 0])
    print(sort)
    sort.sort()
    print(sort)
