from graphinfo import graphinfo

class dijkstra:
    city = graphinfo()
    
    def __init__(self, city):
        self.city = city    

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.city.edges}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.city.edges):
            min_vertex = None
            for vertex in distances:
                if vertex not in visited:
                    if min_vertex is None or distances[vertex] < distances[min_vertex]:
                        min_vertex = vertex

            if min_vertex is None:
                break

            visited.add(min_vertex)

            for neighbor, weight in self.city.get_neighbors(min_vertex):
                if neighbor not in visited:
                    new_distance = distances[min_vertex] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        return distances




