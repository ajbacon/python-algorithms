from weighted_graph import WeightedGraph
import math


def dijkstra_1(graph, start):
    neighbours = graph.get_edges()
    costs = {}
    parents = {}
    visited = [start]
    for k in neighbours.keys():
        costs[k] = math.inf
        parents[k] = None
    costs[start] = 0

    for n in neighbours[start]:
        costs[n[0]] = n[1]
        parents[n[0]] = start

    node = lowest_cost_node(costs, visited)

    while not node == None:
        visited.append(node)
        cost = costs[node]
        for n in g.get_edges()[node]:
            new_cost = cost + n[1]
            if new_cost < costs[n[0]]:
                costs[n[0]] = new_cost
                parents[n[0]] = node

        node = lowest_cost_node(costs, visited)

    print(costs)
    print(parents)


def lowest_cost_node(costs, visited):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if node not in visited and cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


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


dijkstra_1(g, 'A')
