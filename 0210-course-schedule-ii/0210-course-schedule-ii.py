from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        courses = defaultdict(list)
        indegree = [0]*numCourses

        for u, v in prerequisites:
            courses[v].append(u)   # correct direction
            indegree[u] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []

        while q:
            node = q.popleft()     # BFS
            res.append(node)

            for nei in courses[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != numCourses:
            return []

        return res