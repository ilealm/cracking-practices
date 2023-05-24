class Edge:
    def __init__(self, _from, to, weight):
        self._from = _from
        self.to = to
        self.weight = weight

    def __repr__(self):
        return f"{self.to} : {self.weight}"

    def __str__(self):
        return f"{self.to} : {self.weight}"


class Node(Edge):
    def __init__(self, label):
        self.label = label
        # each node will store its adj_list
        self.edges_list = []

    def __repr__(self):
        return f"{self.label}"

    def __str__(self):
        return f"{self.label}"

    def add_edge(self, _from, to, weight):
        new_edge = Edge(_from, to, weight)

        self.edges_list.append(new_edge)


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
        node_from = self.nodes.get(_from)
        node_to = self.nodes.get(to)

        if node_to is None or node_from is None:
            return

        node_from.add_edge(node_from, node_to, weight)
        node_to.add_edge(node_to, node_from, weight)

    def print_edges(self):
        for node, edges in self.nodes.items():
            for edge in edges.edges_list:
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
