class Graph:
    class Node:
        def __init__(self, label):
            self.label = label
            self.next = None

        def __str__(self):
            return f"{self.label} -> {self.next}"

    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def __str__(self):
            return f"Head -> {self.head}"

        def add_node(self, label):
            new_node = Graph.Node(label)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

            return new_node

    def __init__(self):
        self.adj_list = []
        self.hash_table = {}

    def get_num_items_in_adj_list(self):
        return len(self.adj_list)

    def print_adj_list(self):
        for row in self.adj_list:
            print(row)

    def print_hash_table(self):
        for key, value in self.hash_table.items():
            print(key, value)

    def _add_into_adj_list(self, node):
        self.adj_list.append(node)

    def _add_into_hash_table(self, label, index):
        self.hash_table[label] = index

    def add(self, label):
        new_node = self.LinkedList().add_node(label)

        self._add_into_adj_list(new_node)
        self._add_into_hash_table(label, self.get_num_items_in_adj_list() - 1)

        return new_node

    # def add_edge(self, label_from, label_to):
    #     # validate labels
    #     from_node = self.get_node_by_label(label_from)
    #     to_node = self.get_node_by_label(label_to)

    #     if from_node is None or to_node is None:
    #         return

    #     from_node.next = to_node


if __name__ == "__main__":
    import os

    os.system("clear")
    graph = Graph()
    graph.add("John")
    graph.add("Bob")
    graph.add("Mary")
    graph.add("Alice")
    graph.print_adj_list()
    print("\n")
    graph.print_hash_table()
