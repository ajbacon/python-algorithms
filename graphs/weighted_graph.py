class WeightedGraph:
    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        self.edges[node] = []

    def add_edge(self, node_a, node_b, weight):
        self.edges[node_a].append((node_b, weight))
        self.edges[node_b].append((node_a, weight))
        return self.edges

    def get_edges(self):
        return self.edges
