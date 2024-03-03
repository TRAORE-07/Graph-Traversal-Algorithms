# Initialization of a new instance (class Graph).
class Graph:
    def __init__(self, nodes):
        # Takes a list of nodes as input and creates an adjacency list for each node.
        self.nodes = nodes
        self.adjacent_list = {}
        for n in nodes:
            self.adjacent_list[n] = []

    #  Adds an edge from node D to node T.
    def add_edge(self, D, T):
        #  It appends T to the adjacency list of D.
        self.adjacent_list[D].append(T)

    # Implementation of the Breadth-First Search (BFS) algorithm starting from start_node,
    def bfs(self, start_node):
        visited = set()
        # Starting node inserted in the queue.
        queue = [start_node]
        while queue:
            # removing the starting node of the queue after visiting it.
            n = queue.pop(0)
            if n not in visited:
                # Visiting all unvisited nodes.
                visited.add(n)
                for neighbor in self.adjacent_list[n]:
                    # Inserting all the adjacent node of a visited node in the queue.
                    queue.append(neighbor)
        return visited

    # Implements the Depth-First Search (DFS) algorithm starting from start_node,
    # It returns a set of all nodes reachable from start_node.
    def dfs(self, start_node):
        # visited arrays are empty.
        visited = set()
        # starting node inserted in the stack.
        stack = [start_node]
        while stack:
            # removing of the visited node of the stack after visiting it.
            node = stack.pop()
            if node not in visited:
                # Visiting all unvisited node.
                visited.add(node)
                for neighbor in self.adjacent_list[node]:
                    # Inserting all the adjacent node of a visited node in the stack.
                    stack.append(neighbor)
        return visited

    # Checks if the graph is connected.
    # It does this by performing a DFS from the first-node,
    # and then checking if the number of visited nodes is equal to the total number of nodes.
    def connectivity(self):
        # Returning a list of nodes that were visited during the DFS.
        visited = self.dfs(self.nodes[0])
        # Checking if the number of visited nodes is equal to the total number of nodes in the graph.
        return len(visited) == len(self.nodes)


nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
my_graph = Graph(nodes)
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('B', 'E')
my_graph.add_edge('C', 'D')
my_graph.add_edge('E', 'G')
my_graph.add_edge('G', 'H')

# BFS applied in the graph starting with the node 'A'.
print("Using BFS: ", my_graph.bfs('A'))
# DFS applied in the graph starting with the node 'A'.
print("Using DFS: ", my_graph.dfs('A'))
# Checking if all the nodes of the graph are connected.
print("The given graph is Connected: ", my_graph.connectivity())