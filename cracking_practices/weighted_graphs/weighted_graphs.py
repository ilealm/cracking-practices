from collections import deque
from queue import PriorityQueue
import math


class Path:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def __str__(self):
        return str.join(" ", self.nodes)


# encapsulating a node so I can get access to its priority as a method, instead as a property
class NodeEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    # def __repr__(self) -> str:
    def __repr__(self):
        return f"Node {self.node.label} priority {self.priority}"

    def __str__(self):
        return f"Node {self.node.label} priority {self.priority}"

    # method is a special method that is used to define the behavior of the less-than operator
    def __lt__(self, other):
        return self.priority < other.priority


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



    def get_shortest_path(self, from_label, to_label):

        if not from_label in  self.nodes.keys() or not to_label in  self.nodes.keys():
            return ""


        from_node = self.nodes[from_label]
        to_node = self.nodes[to_label]



        distances = {}
        infinite = math.inf
        # set to keep track of the visited nodes
        visited = set()
        previous_nodes = {}
        # all the items in the queue are nodeEntry objs
        queue = PriorityQueue()

        # load the nodes into distances hashTable
        for node in self.nodes.values():
            distances[node] = infinite

        # set the distance of the starting node to zero
        distances[from_node] = 0

        # here I can pass 0 BC its the only item in the queue
        ne = NodeEntry(from_node, 0)
        queue.put(ne)

        # depth first traveral
        while not queue.empty():
            current = queue.get().node
            visited.add(current)
            # look to all it unvisited neighbors
            for edge in current.get_edges():
                if edge in visited:
                    continue

                # calculate the new distance
                new_distance = distances[current] + edge.weight
                if new_distance < distances[edge.to]:
                    distances[edge.to] = new_distance
                    previous_nodes[edge.to] = current
                    ne = NodeEntry(edge.to, new_distance)
                    queue.put(ne)
                    # queue.put(NodeEntry(edge.to, new_distance))

        return self.build_path(to_node, previous_nodes)

    def build_path(self, to_node, previous_nodes):
        stack = deque()
        stack.append(to_node)
        previous = previous_nodes[to_node]
        while not previous is None:
            stack.append(previous)
            if previous in previous_nodes.keys():
                previous = previous_nodes[previous]
            else:
                previous = None

        path = Path()
        while stack:
            path.add_node(stack.pop().label)

        return path.__str__()


if __name__ == "__main__":
    import os

    os.system("clear")

    g = WightedGraph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")

    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 2)
    g.add_edge("A", "C", 10)

    # g.print_edges()
    x = g.get_shortest_path("A", "K")
    print(x)
    # for item in x.nodes:
    #     print(item)


# pq = PriorityQueue()
# pq.put((3, Node("three")))
# pq.put((10, Node("ten")))
# pq.put((2, Node("two")))
# while not pq.empty():
#     print(pq.get())


# asd
