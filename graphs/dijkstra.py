from weighted_graph import WeightedGraph


def dijkstra_1(graph, start, end):
    pass


def find_next_node():
    pass



g = WeightedGraph()

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')

g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 8)
g.add_edge('B', 'D', 4)
g.add_edge('B', 'E', 2)
g.add_edge('C', 'E', 7)
g.add_edge('D', 'E', 6)
g.add_edge('D', 'F', 3)
g.add_edge('E', 'F', 1)

print(g.get_edges())

# dijkstra_1(example_graph, 'A')
