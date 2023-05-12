class Graph:
    class LinkedList:
        class Node:
            def __init__(self, label):
                self.label = label
                self.next = None

            def __str__(self):
                return f"{self.label} -> {self.next}"

        def __init__(self):
            self.head = None
            self.tail = None

        def __str__(self):
            return f"Head -> {self.head}"

        def add_node(self, label):
            new_node = self.Node(label)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

            return new_node

        def get_head(self):
            return self.head



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
        new_LL = self.LinkedList()
        new_node = new_LL.add_node(label)

        # new_node = self.LinkedList().add_node(label)

        # self._add_into_adj_list(new_node)
        self._add_into_adj_list(new_LL)
        # todo lower case label
        self._add_into_hash_table(
            self.groom_word(label), self.get_num_items_in_adj_list() - 1
        )

        return new_node

    def get_label_index(self, label):
        label = self.groom_word(label)
        if not label in self.hash_table.keys():
            return None

        return self.hash_table[label]

    def get_node_by_label(self, label):
        index = self.get_label_index(label)

    def groom_word(self, word):
        return word.lower().strip()

    def add_edge(self, label_from, label_to):
        #     # validate labels
        index_from = self.get_label_index(label_from)
        index_to = self.get_label_index(label_to)

        if index_from is None or index_to is None:
            return

        current = self.adj_list[index_from]
        # print(current)
        current.add_node(label_to)
        # print(current)

        # print(
        #     " \nAdd Edge from ",
        #     label_from,
        #     "[",
        #     index_from,
        #     "]",
        #     " to ",
        #     label_to,
        #     "[",
        #     index_to,
        #     "]\n",
        # )




if __name__ == "__main__":
    import os

    os.system("clear")
    graph = Graph()
    graph.add("John")
    graph.add("Bob")
    graph.add("Mary")
    graph.add("Alice")
    # graph.print_adj_list()
    print("\n")
    graph.print_hash_table()

    graph.add_edge("John", "mary")
    graph.add_edge("John", "bob")
    graph.add_edge("alice", "bob")
    graph.add_edge("bob", "john")
    graph.add_edge("bob", "john")


    graph.print_adj_list()

