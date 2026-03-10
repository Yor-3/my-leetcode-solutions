class dij:
    def __init__(self,n,edges,directed=True):
        self.n = n
        self.graph =defaultdict(list)
        for u,v,w in edges:
            self.graph[u].append((v,w))
            if not directed:
                self.graph[v].append((u,w))

    def shortest_path(self,src):
        dist = [float('inf')] * (self.n + 1)
        pq = []
        for s in src:
            dist[s] = 0
            heapq.heappush(pq,(0,s))
        while pq:
            cur_dist,node = heapq.heappop(pq)
            if cur_dist>dist[node]:
                continue

            for nei,w in self.graph[node]:
                new_dist = cur_dist+w

                if new_dist<dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(pq,(new_dist,nei))

        return dist

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dis = dij(n,times)
        ans = max(dis.shortest_path([k])[1:])
        return -1 if (ans == float('inf')) else ans