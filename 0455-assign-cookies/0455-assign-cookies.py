class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n,m = len(g),len(s)
        i,j =0,0
        g.sort()
        s.sort()
        res= 0
        while (i in range(n)) and (j in range(m)):
            if g[i] <= s[j]:
                res +=1
                i+=1
                j+=1
            elif g[i]>s[j]:
                j+=1

        return res