class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[-1 for _ in range(n)]for _ in range(m)]
        # dp[0][0] = 1
        # for i in range(1,n):
        #     dp[0][i] = 1

        # for j in range(1,m):
        #     dp[j][0] = 1
        temp = [1]*n
        for i in range(1,m):
            cur = [1]*n
            for j in range(1,n):
                
                cur[j] = (cur[j-1])+(temp[j]  ) 

            temp = cur

        return temp[n-1]
        