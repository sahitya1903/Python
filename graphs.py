from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour, _ in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)
        print()

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            v = queue.pop(0)
            print(v, end=' ')
            for neighbour, _ in self.graph[v]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        print()

    def prim_mst(self):
        start_node = next(iter(self.graph))
        visited = set([start_node])
        edges = [
            (weight, start_node, to)
            for to, weight in self.graph[start_node]
        ]
        heapq.heapify(edges)
        mst = []
        while edges:
            weight, frm, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                mst.append((frm, to, weight))
                for to_next, weight in self.graph[to]:
                    if to_next not in visited:
                        heapq.heappush(edges, (weight, to, to_next))
        return mst

# Example usage:
g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 2)
g.add_edge(4, 5, 6)

print("DFS starting from vertex 0:")
g.dfs(0)

print("BFS starting from vertex 0:")
g.bfs(0)

print("Prim's MST:")
mst = g.prim_mst()
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")