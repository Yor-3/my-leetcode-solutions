class Unionfind:

    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1] * (n+1)
        self.components = n

    def find(self, x):

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # path compression

        return self.parent[x]

    def union(self, a, b):

        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False  # cycle detected

        # union by rank
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        elif self.rank[pb] > self.rank[pa]:
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1

        self.components -= 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = Unionfind(len(edges))
        for u,v in edges:
            if not uf.union(u,v):
                return [u,v]