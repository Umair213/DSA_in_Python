# Implementing adjacency list representation with simple and undirected Graph.

class Graph:
    def __init__(self, v_size):
        self.vertex_size = v_size
        self.adj_list = {x: [] for x in range(v_size)}

    # Add edge between vertexes u and v with weight
    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertex_size and 0<=v<self.vertex_size:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Vertex is not correct")

    # Remove edge between vertexes u and v
    def remove_edge(self, u, v):
        if 0<=u<self.vertex_size and 0<=v<self.vertex_size:
            for key, value in self.adj_list.items():
                if key == u:
                    for item in value:
                        if v == item[0]:
                            value.remove(item)
                elif key == v:
                    for item in value:
                        if u == item[0]:
                            value.remove(item)

    # Check if the vertexes has edge
    def has_edge(self, u, v):
        if 0<=u<self.vertex_size and 0<=v<self.vertex_size:
            if v in self.adj_list[u][0]:
                return True

    # Print adjacent list
    def print_adj_list(self):
        for lst in self.adj_list.values():
            print(lst)

graph_obj = Graph(4)
graph_obj.add_edge(0, 1, 5)
graph_obj.add_edge(3, 1, 9)
print(graph_obj.has_edge(0, 1))
graph_obj.print_adj_list()
graph_obj.remove_edge(3, 1)
print("\n")
graph_obj.print_adj_list()