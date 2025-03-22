class Solution:
    def canFinish(self, v: int, prerequisites: List[List[int]]) -> bool:
        premap = {
            i:[] for i in range(v)
        }
        vis = set()
        
        for crs,pre in prerequisites:
            premap[crs].append(pre)

        def dfs(crs):
            if crs in vis:
                return False

            if premap[crs] == []:
                return True

            vis.add(crs)
            for n in premap[crs]:
                if not dfs(n):
                    return False

            vis.remove(crs)

            premap[crs] = []

            return True


        for i in range(v):
            if not dfs(i):
                return False

        return True
            

                


