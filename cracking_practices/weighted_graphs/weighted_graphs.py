from queue import PriorityQueue


class Edge:
    def __init__(self, _from, to, weight):
        self._from = _from
        self.to = to
        self.weight = weight

    def __repr__(self):
        return f"{self.to} : {self.weight}"

    def __str__(self):
        return f"{self.to} : {self.weight}"


class Node:
    def __init__(self, label):
        self.label = label
        self.edges_list = []

    def __repr__(self):
        return f"{self.label}"

    def __str__(self):
        return f"{self.label}"

    def add_edge(self, target, weight):
        new_edge = Edge(self, target, weight)

        self.edges_list.append(new_edge)

    def get_edges(self):
        return self.edges_list


class WightedGraph:
    def __init__(self):
        self.nodes = {}

    def _key_already_exist_in_nodes(self, key):
        return key in self.nodes.keys()

    def _key_already_exist_in_adj_list(self, key):
        return key in self.nodes.keys()

    def add_node(self, label):
        new_node = Node(label)
        if not self._key_already_exist_in_nodes(label):
            self.nodes[label] = new_node

    def add_edge(self, _from, to, weight):
        from_node = self.nodes.get(_from)
        to_node = self.nodes.get(to)

        if to_node is None or from_node is None:
            return

        from_node.add_edge(to_node, weight)
        to_node.add_edge(from_node, weight)

    def print_edges(self):
        for node in self.nodes.values():
            for edge in node.get_edges():
                print(node, "->", edge)


if __name__ == "__main__":
    import os

    os.system("clear")

    g = WightedGraph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")

    g.add_edge("A", "B", 3)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 20)
    g.print_edges()


# pq = PriorityQueue()
# pq.put((3, Node("three")))
# pq.put((10, Node("ten")))
# pq.put((2, Node("two")))
# while not pq.empty():
#     print(pq.get())


# asd
