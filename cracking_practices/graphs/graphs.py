# iris approach
class Graph_textbook_approach:
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
        # return word.lower().strip()
        return word.strip()

    def add_edge(self, label_from, label_to):
        #     # validate labels
        index_from = self.get_label_index(label_from)
        index_to = self.get_label_index(label_to)

        if index_from is None or index_to is None:
            return

        current = self.adj_list[index_from]
        current.add_node(label_to)


# Idea is to have two hash_tables, one for the label with their nodes,
# and the other with the edges of each node
# nodes hash_table
#   label : nodes
#    John : <node kfnksgkdbff>
#    Bob  : <node kdgdfjgdfjh>
#    Mary : <node swetksbhfdk>

# adj_list hash_table. AKA where the edges will be stored
#   node : [list of nodes]
# <node_John kfnksgkdbff> : [<node_Mary kdgdfjgdfjh>,  <node_Bob kdgdfjgdfjh>]


class Graph:
    class Node:
        def __init__(self, label):
            self.label = label

        def __str__(self):
            return f"{self.label}"

    def __init__(self):
        self.nodes = {}
        # adj_list -> node : list[nodes]
        self.adj_list = {}

    # def _key_already_exist(self, hash_table, key):
    def _key_already_exist_in_nodes(self, key):
        return key in self.nodes.keys()

    def _key_already_exist_in_adj_list(self, key):
        return key in self.adj_list.keys()

    def add_node(self, label):
        node = self.Node(label)

        # if not self._key_already_exist(self.nodes, label):
        if not self._key_already_exist_in_nodes(label):
            self.nodes[label] = node

        # if not self._key_already_exist(self.adj_list, label):
        if not self._key_already_exist_in_adj_list(label):
            self.adj_list[node] = []

    def add_edge(self, from_label, to_label):
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)

        if (from_node is None) or (to_node is None):
            raise Exception("Not a valid node")

        self.adj_list.get(from_node).append(to_node)


    # this method remove the node and the edges that it has
    def removeNode(self, label):
        node_to_delete = self.nodes.get(label)

        if node_to_delete is None:
            return

        # remove edges
        for key, edges_list in self.adj_list.items():
            if node_to_delete in edges_list:
                edges_list.remove(node_to_delete)

        # remove the node from the edges dictionary
        self.adj_list.pop(node_to_delete)




    def print_edges(self):
        for key, value in self.adj_list.items():
            for edge in value:
                print(key.label)
                print(" -> ", edge.label)


# if __name__ == "__main__":
#     import os

#     os.system("clear")
#     graph = Graph()
#     graph.add_node("John")
#     graph.add_node("Mary")
#     graph.add_node("Bob")
#     graph.add_node("Alice")
#     graph.add_node("Dan")
#     graph.add_node("Nina")

#     graph.add_edge("John", "Mary")
#     graph.add_edge("John", "Bob")
#     graph.add_edge("Bob", "John")
#     graph.add_edge("Mary", "John")
#     graph.add_edge("Alice", "Mary")
#     graph.add_edge("Dan", "Nina")
#     graph.print_edges()
#     print("\n")
#     graph.removeNode("John")
#     graph.print_edges()

