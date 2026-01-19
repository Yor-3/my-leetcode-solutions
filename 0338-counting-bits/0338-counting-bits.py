class Solution:
    def countBits(self, n: int) -> List[int]:
        def getbits(n):
            res = 0
            while n:
                n=n&(n-1)
                res+=1
            return res
        ans = []
        for i in range(n+1):
            ans.append(getbits(i))

        return ans

        