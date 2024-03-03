class Graph:
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph_dict[node]:
                    stack.append(neighbor)
        return visited

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": ["E"],
        "E": [],
    }

    start_node = "A"
    g = Graph(graph)
    print(g.dfs(start_node))
