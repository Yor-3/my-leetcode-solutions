class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(2)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
                else:
                    dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

        i, j = n, m
        res = []
        full_dp = [[0] * (m + 1) for _ in range(n + 1)]

        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if s1[x - 1] == s2[y - 1]:
                    full_dp[x][y] = 1 + full_dp[x - 1][y - 1]
                else:
                    full_dp[x][y] = max(full_dp[x - 1][y], full_dp[x][y - 1])

        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                res.append(s1[i - 1])
                i -= 1
                j -= 1
            elif full_dp[i - 1][j] > full_dp[i][j - 1]:
                res.append(s1[i - 1])
                i -= 1
            else:
                res.append(s2[j - 1])
                j -= 1

        while i > 0:
            res.append(s1[i - 1])
            i -= 1
        while j > 0:
            res.append(s2[j - 1])
            j -= 1

        return ''.join(reversed(res))
