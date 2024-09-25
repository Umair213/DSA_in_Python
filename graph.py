# Implementing adjacency matrix representation with simple and undirected Graph. 

class Graph:
    def __init__(self, v_count):
        self.vertex_count = v_count
        self.adj_matrix = [[0]*v_count for number in range(v_count)] # made v_count * v_count matrix

    # Add edge between vertexes u and v with weight
    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")

    # Remove edge between vertexes u and v
    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")

    # Check if the vertexes has edge
    def has_edge(self, u, v):
        return self.adj_matrix[u][v] != 0

    # Print adjacent matrix
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            list_of_strings = map(str, row_list)
            print(" ".join(list_of_strings))

graph_obj = Graph(5)
graph_obj.add_edge(0, 1, 5)
graph_obj.add_edge(3, 1, 9)
print(graph_obj.has_edge(0, 1))
graph_obj.print_adj_matrix()
graph_obj.remove_edge(3, 1)
print("\n")
graph_obj.print_adj_matrix()