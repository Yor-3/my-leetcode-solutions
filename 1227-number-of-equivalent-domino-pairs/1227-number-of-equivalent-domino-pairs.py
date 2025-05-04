class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cont =defaultdict(int)
        for a,b in dominoes:
            key = (min(a,b),max(a,b))

            cont[key]+=1

        res = 0
        for p in cont.values():
            if p>=2:

                res+= ((p)*(p-1)//2)

        return res
