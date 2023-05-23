class WightedGraph:
    class Node:
        def __init__(self, label):
            self.label = label

        def __repr__(self):
            # def __str__(self):
            return f"{self.label}"

    class Edge:
        # from and to are Node objects
        def __init__(self, _from, to, weight):
            self._from = _from
            self.to = to
            self.weight = weight

        # def __repr__(self):
        def __str__(self):
            # return f"{self._from} -> {self.to}"
            return f"{self._from} -> {self.to} : {self.weight}"

    def __init__(self):
        self.nodes = {}
        # node  : list of edges:
        self.adj_list = {}

    def _key_already_exist_in_nodes(self, key):
        return key in self.nodes.keys()

    def _key_already_exist_in_adj_list(self, key):
        return key in self.adj_list.keys()

    def add_node(self, label):
        new_node = self.Node(label)
        if not self._key_already_exist_in_nodes(label):
            self.nodes[label] = new_node

        if not self._key_already_exist_in_adj_list(label):
            self.adj_list[new_node] = []

    def add_edge(self, _from, to, weight):
        # # this graph is undirected, so I need to have the edges _from -> to, and to -> _from

        node_from = self.nodes.get(_from)
        node_to = self.nodes.get(to)

        if node_to is None or node_from is None:
            return

        edge_from = self.Edge(node_from, node_to, weight)
        edge_to = self.Edge(node_to, node_from, weight)

        self.adj_list.get(node_from).append(edge_from)
        self.adj_list.get(node_to).append(edge_to)

    def print_edges(self):
        for node, adj_list in self.adj_list.items():
            print(node, "connections:")
            for edge in adj_list:
                print("    ", edge)


if __name__ == "__main__":
    import os

    os.system("clear")

    g = WightedGraph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    # g.add_node('D')

    g.add_edge("A", "B", 3)
    g.add_edge("A", "C", 2)
    g.print_edges()
