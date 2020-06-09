from collections import deque


def short_path_bfs(graph, start, finish):
    print('here')
    path = {
        start: None
    }
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()
        visited.append(current)
        for neighbour in graph[current]:
            if neighbour not in path:
                queue.append(neighbour)
                path[neighbour] = current

    path_trace = [finish]
    next_node = path[finish]
    while next_node:
        path_trace.append(next_node)
        next_node = path[next_node]

    return path_trace[::-1]


graph = {
    'A': ["B", "C"],
    'B': ["A", "C", "D", "E"],
    'C': ["A", "B", "D"],
    'D': ["B", "C", "E", "F"],
    'E': ["B", "D"],
    'F': ["D"]
}

print(short_path_bfs(graph, 'A', 'F'))
