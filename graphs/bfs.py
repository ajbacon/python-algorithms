from test import *
from collections import deque


def breadth_first_search_1(graph, start):
    visited = [start]
    search_queue = deque()
    search_queue.extend(graph[start])
    print(f'visited: {start}')
    while search_queue:
        current = search_queue.popleft()
        if not current in visited:
            print(f'visited: {current}')
            visited.append(current)
            search_queue.extend(graph[current])


example_graph = {
    'A': ['B', 'C'],
    'B': ['E'],
    'C': ['D'],
    'D': ['E'],
    'E': ['F'],
    'F': []
}

breadth_first_search_1(example_graph, 'A')
