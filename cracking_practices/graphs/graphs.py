import queue
from collections import deque

# Idea is to have two hash_tables: One for the label with their nodes,
# and the other with the edges of each node
# nodes hash_table:
#    LABEL: <NODE>
#    John : <node kfnksgkdbff>
#    Bob  : <node kdgdfjgdfjh>
#    Mary : <node swetksbhfdk>

# adj_list hash_table. AKA where the edges will be stored
#   NODE : [LIST OF NODES WHERE THE NODE HAS EDGES]
#   <node_John kfnksgkdbff> : [<node_Mary kdgdfjgdfjh>,  <node_Bob kdgdfjgdfjh>]


class Graph:
    class Node:
        def __init__(self, label):
            self.label = label

        def __str__(self):
            return f"{self.label}"

    def __init__(self):
        self.nodes = {}
        self.adj_list = {}

    def _key_already_exist_in_nodes(self, key):
        return key in self.nodes.keys()

    def _key_already_exist_in_adj_list(self, key):
        return key in self.adj_list.keys()

    def add_node(self, label):
        node = self.Node(label)

        if not self._key_already_exist_in_nodes(label):
            self.nodes[label] = node

        if not self._key_already_exist_in_adj_list(label):
            self.adj_list[node] = []

    def add_edge(self, from_label, to_label):
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)

        if (from_node is None) or (to_node is None):
            raise Exception("Not a valid node")

        self.adj_list.get(from_node).append(to_node)

    def remove_edge(self, from_label, to_label):
        from_node = self.nodes.get(from_label)
        to_node = self.nodes.get(to_label)

        if (from_node is None) or (to_node is None):
            return

        self.adj_list.get(from_node).remove(to_node)

    # this method remove the node and the edges that it has
    def remove_node(self, label):
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

    def _get_randon_node(self):
        keys = list(self.nodes.keys())

        if len(keys) == 0:
            return None

        return self.nodes[keys[0]]

    def get_neighbors(self, node):
        return self.adj_list[node]

    def traverse_breath(self):
        # set (no dupplicates allowed) of visited nodes
        visited_nodes = set()
        queue_nodes = queue.Queue()

        # get a node to start the process
        current = self._get_randon_node()

        if current is None:
            return None

        # add node to queue
        queue_nodes.put(current)
        while not queue_nodes.empty():
            current = queue_nodes.get()
            # print("visiting ", current.label)
            # add node to set
            visited_nodes.add(current.label)
            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                if not neighbor.label in visited_nodes:
                    queue_nodes.put(neighbor)

        return visited_nodes

    def _get_node_by_label(self, label):
        return self.nodes[label]

    # depth first with stack approach
    def topological_sort(self):
        stack = deque()
        visited_nodes = set()

        def traverse(current, visited_nodes, stack):
            if current in visited_nodes:
                return

            visited_nodes.add(current)

            neighbors = self.get_neighbors(current)

            for neighbor in neighbors:
                traverse(neighbor, visited_nodes, stack)

            stack.append(current.label)

        # in order to ensure I traverse all the nodes, Im using a death first on all the nodes
        for node in self.nodes.values():
            traverse(node, visited_nodes, stack)

        stack.reverse()

        return list(stack)

    def is_empty(self, object):
        return len(object) == 0



    def has_cycle(self):
        all_nodes = set(self.nodes.values())

        if self.is_empty(all_nodes):
            return False

        visiting = set()
        visited = set()

        # pick a node from all_nodes set and start the traversal
        # if I find a cycle, return True. Otherwise keep traversing

        def traverse(node, all_nodes, visiting, visited):
                # move the fist nodes from the first set, to the second set
                all_nodes.remove(node)
                visiting.add(node)

                # visit all the neighbors of this node
                for neighbor in self.get_neighbors(node):
                    if neighbor in visited:
                        continue

                    if neighbor in visiting:
                        return True

                    if traverse(neighbor, all_nodes, visiting, visited):
                        return True

                # if I got to this point means I haven't found a cycle in the current node
                visiting.remove(node)
                visited.add(node)

                return False


        while not self.is_empty(all_nodes):
            current = list(all_nodes)[0]
            if traverse(current, all_nodes, visiting, visited):
                return True

        return False



# if __name__ == "__main__":
#     import os

#     os.system("clear")
#     graph = Graph()
#     graph.add_node("A")
#     graph.add_node("B")
#     graph.add_node("C")

#     graph.add_edge("A", "B")
#     graph.add_edge("B", "C")
#     # graph.add_edge("C", "A")
#     graph.add_edge("A", "C")

#     # print(graph.print_edges())
#     print(graph.has_cycle())

