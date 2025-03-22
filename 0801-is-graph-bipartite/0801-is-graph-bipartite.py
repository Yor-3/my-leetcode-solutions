class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        col = [-1]* len(graph) 
        
   
        def dfs(node,color):
            
            
            col[node] = color
            

            for n in graph[node]:
                if col[n]==-1:
                    if not dfs(n,1-color):
                        return False

                elif col[n] == col[node]:
                    return False

            

            return True

        for i in range(len(graph)):
            if col[i]==-1:
                if not dfs(i,0):
                    return False

        return True