class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp_next = [[0] * cols for _ in range(cols)]

        for col1 in range(cols):
            for col2 in range(cols):
                if col1 == col2:
                    dp_next[col1][col2] = grid[rows-1][col1]
                else:
                    dp_next[col1][col2] = grid[rows-1][col1] + grid[rows-1][col2]

        for row in range(rows-2, -1, -1):
            dp_curr = [[0] * cols for _ in range(cols)]
            for col1 in range(cols):
                for col2 in range(cols):
                    max_cherries = float('-inf')
                    for d1 in [-1, 0, 1]:
                        for d2 in [-1, 0, 1]:
                            new_col1 = col1 + d1
                            new_col2 = col2 + d2
                            if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                                max_cherries = max(max_cherries, dp_next[new_col1][new_col2])
                    if col1 == col2:
                        dp_curr[col1][col2] = grid[row][col1] + max_cherries
                    else:
                        dp_curr[col1][col2] = grid[row][col1] + grid[row][col2] + max_cherries
            dp_next = dp_curr

        return dp_next[0][cols-1]
