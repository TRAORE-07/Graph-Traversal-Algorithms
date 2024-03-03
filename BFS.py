from collections import deque

def bfs(graph, n):
    visited = set()
    queue = deque([n])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
    return visited

if __name__ == "__main__":
    graph = {
        "C": ["A", "D"],
        "D": ["C", "E"],
        "A": ["C", "B"],
        "B": ["A", "E"],
        "E": ["B", "D"]
    }

    n = "C"

    bfs(graph, n)
