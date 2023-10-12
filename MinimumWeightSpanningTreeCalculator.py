import re  # Import the regex library
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]  # Initialize up to n + 1
        self.rank = [0 for _ in range(n + 1)]  # Initialize up to n + 1

    
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
      
      
      
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            else:
                self.parent[rootU] = rootV
                if self.rank[rootU] == self.rank[rootV]:
                    self.rank[rootV] += 1

def kruskal(n, edges):
    edges.sort(key=lambda edge: edge[2])  # Sort edges by weight
    uf = UnionFind(n + 1)  # Pass n + 1 to the constructor
    mst_weight = 0.0
    for edge in edges:
        u, v, w = edge
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += w
    return mst_weight


def main():
    with open("10.txt", "r") as f:
        edges = []
        max_vertex = -1
        content = f.read().strip("{}")  # Read whole content and strip outer braces
        for line in content.split("}, {"):  # Split based on edge representation
            numbers = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', line)
            u, v, w = map(float, numbers)
            u, v = int(u), int(v)
            edges.append((u, v, w))
            max_vertex = max(max_vertex, u, v)
        
        mst_weight = kruskal(max_vertex, edges)
        print(f"Weight of the MST: {mst_weight:.4f}")

if __name__ == "__main__":
    main()
