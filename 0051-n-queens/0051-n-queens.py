class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pd = set()
        nd = set()
        res = []
        board = [['.'] *n for i in range(n)]

        def help(r):
            if r==n:
                copy = ["".join(x) for x in board]
                res.append(copy)
                return 

            for c in range(n):
                if c in col or (r-c) in nd or (r+c) in pd:
                    continue

                col.add(c)
                nd.add(r-c)
                pd.add(r+c)
                board[r][c] ="Q"

                help(r+1)

                col.remove(c)
                nd.remove(r-c)
                pd.remove(r+c)

                board[r][c] ="."

        help(0)

        return res