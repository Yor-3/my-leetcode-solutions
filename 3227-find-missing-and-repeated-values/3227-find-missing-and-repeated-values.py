class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dct = {}

        n = len(grid)**2+1

        for row in grid:
            for val in row:
                dct[val] = dct.get(val,0)+1

        lst = [0,0]

        for i in range(1,n):
            val = dct.get(i,0)
            if val>1:
                lst[0] = i

            if val == 0:
                lst[1] = i

        return lst