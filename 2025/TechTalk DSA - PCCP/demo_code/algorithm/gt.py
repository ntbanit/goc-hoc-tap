from collections import deque

# Graph represented using an adjacency list
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        # Add edge u -> v
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

        # Add edge v -> u (for undirected graph)
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append(u)

    def display(self):
        for key, value in self.adj_list.items():
            print(f"{key}: {value}")

    # Depth-First Search (DFS)
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Breadth-First Search (BFS)
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Example Usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    print("Graph (Adjacency List):")
    g.display()

    print("\nDFS Traversal:")
    g.dfs(0)

    print("\n\nBFS Traversal:")
    g.bfs(0)