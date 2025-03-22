from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows,cols = len(grid),len(grid[0])
        vis = set()

        res = 0
        
        def bfs(R,C):
            q = deque()
            vis.add((R,C))
            q.append((R,C))

            while q:
                row,col = q.popleft()

                direc = [[1,0],[0,1],[-1,0],[0,-1]]

                for dr,dc in direc:
                    r,c= row+dr,col+dc
                    if (r in range(rows) and (c in range(cols) and grid[r][c]=='1' and (r,c) not in vis )):
                        vis.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in vis:
                    bfs(r,c)
                    res+=1

        return res