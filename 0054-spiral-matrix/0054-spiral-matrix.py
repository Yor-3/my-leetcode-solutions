class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r=0,len(matrix[0])
        u,d = 0,len(matrix)
        res = []
        while l<r and u<d:
            for i in range(l,r):
                res.append(matrix[u][i])

            u+=1

            for i in range(u,d):
                res.append(matrix[i][r-1])

            r=r-1

            if not (u<d and l<r): 
                break

            for i in range(r-1,l-1,-1):
                res.append(matrix[d-1][i])

            d-=1
            for i in range(d-1,u-1,-1):
                res.append(matrix[i][l])
            l+=1

        return res
                
        return 