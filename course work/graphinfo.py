class graphinfo:
    def __init__(self):
        self.edges = {} 
        self.districts = {}
        
    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, weight))
    
    def add_district(self, u, importance):
        if u not in self.districts:
            self.districts[u] = 0
        self.districts[u] += importance
        
    def get_neighbors(self, vertex):
        return self.edges.get(vertex, [])
    
    def get_importance(self, u):
        return self.districts[u]

    def __str__(self):
        result = []
        for vertex, neighbors in self.edges.items():
            result.append(f"{vertex} (importance-{self.districts[vertex]}): {', '.join([f'({n[0]}, {n[1]})' for n in neighbors])}")
        return "\n".join(result)




