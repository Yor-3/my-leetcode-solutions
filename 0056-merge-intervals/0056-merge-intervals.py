class Solution:
    def merge(self, i: List[List[int]]) -> List[List[int]]:
        i.sort(key = lambda x:x[0])

        res = [i[0]]

        for s,e in i:
            last = res[-1][1]

            if s<=last:
                res[-1][1] = max(last,e)
            else:
                res.append([s,e])

        return res