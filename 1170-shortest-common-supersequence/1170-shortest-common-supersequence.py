class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Find starting common sequence.  If common start 
        # covers all of one or both of the strings, then 
        # return the common start string plus any remnants 
        # of the other string.
        cmnStart = ""
        n = min(len(str1), len(str2))
        i = 0
        while i < n and str1[i] == str2[i]:  i += 1
        if i == n:  
            return "".join([str1[:i], str1[i:], str2[i:]])

        # Find ending common sequence.
        cmnEnd = ""
        n -= i
        j = 1
        while j < n and str1[-j] == str2[-j]:  j += 1
        j -= 1

        # After finding common start and common end of strings, 
        # remove the common start and end of the strings.
        if i > 0 or j > 0:
            if i > 0:  cmnStart = str1[:i]
            if j > 0:  cmnEnd = str1[-j:]
            str1 = str1[i: len(str1) - j]
            str2 = str2[i: len(str2) - j]
        n1 = len(str1)
        n2 = len(str2)

        # Find longest common sequence using DP.
        sc1 = list(map(ord, str1))
        sc2 = list(map(ord, str2))
        dp = [[0]*(n2 + 1) for _ in range(n1 + 1)]
        for i1 in range(n1 + 1):  dp[i1][0] = i1
        dp[0] = list(range(n2 + 1))

        for i1,ch1 in enumerate(sc1):
            for i2,ch2 in enumerate(sc2):
                dp[i1 + 1][i2 + 1] = 1 + (dp[i1][i2] if ch1 == ch2 else min(dp[i1 + 1][i2], dp[i1][i2 + 1]))
        
        # Build result string from backtracking through DP 
        # for longest common sequence.
        i1 = n1 - 1
        i2 = n2 - 1
        result = [cmnEnd]
        while i1 >= 0 and i2 >= 0:
            if sc1[i1] == sc2[i2]:
                result.append(str1[i1])
                i1 -= 1
                i2 -= 1
            elif dp[i1 + 1][i2 + 1] == dp[i1][i2 + 1] + 1:
                result.append(str1[i1])
                i1 -= 1
            else:
                result.append(str2[i2])
                i2 -= 1
        
        if i2 >= 0:  result.append(str2[: i2 + 1])
        if i1 >= 0:  result.append(str1[: i1 + 1])
        result.append(cmnStart)
        return "".join(reversed(result))

