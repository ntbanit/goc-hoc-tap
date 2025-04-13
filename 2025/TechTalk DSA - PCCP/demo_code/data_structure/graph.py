# 1. Adjacency Matrix
class AdjacencyMatrixGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight  # For undirected graph

    def display(self):
        for row in self.matrix:
            print(row)


# 2. Adjacency List
class AdjacencyListGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # For undirected graph

    def display(self):
        for key, value in self.adj_list.items():
            print(f"{key}: {value}")




# Example Usage
if __name__ == "__main__":
    print("Adjacency Matrix:")
    adj_matrix_graph = AdjacencyMatrixGraph(4)
    adj_matrix_graph.add_edge(0, 1)
    adj_matrix_graph.add_edge(1, 2)
    adj_matrix_graph.display()

    print("\nAdjacency List:")
    adj_list_graph = AdjacencyListGraph(4)
    adj_list_graph.add_edge(0, 1)
    adj_list_graph.add_edge(1, 2)
    adj_list_graph.display()

