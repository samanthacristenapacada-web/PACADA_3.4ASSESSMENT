from collections import deque


# Graph using PACADA
graph = {
    "D": ["P", "A1"],
    "P": ["D", "C", "A2"],
    "A1": ["D", "A3"],
    "C": ["P"],
    "A2": ["P", "A3"],
    "A3": ["A2", "A1"]
}


# Display Graph without traversal
def display_graph(graph):
    print("GRAPH CONNECTIONS")

    for vertex, neighbors in graph.items():
        print(vertex, "<->", ", ".join(neighbors))


# BFS Traversal
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# DFS Traversal
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
