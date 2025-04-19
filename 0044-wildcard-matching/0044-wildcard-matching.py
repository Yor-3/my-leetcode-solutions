class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        n1, n2 = len(text), len(pattern)
        prev = [False] * (n2 + 1)
        curr = [False] * (n2 + 1)
        prev[0] = True

        for j in range(1, n2 + 1):
            if pattern[j - 1] == '*':
                prev[j] = prev[j - 1]

        if n2 == 0 and n1 > 0:
            return False

        for i in range(1, n1 + 1):
            flag = all(pattern[k - 1] == '*' for k in range(1, n2 + 1))
            curr[0] = flag

            for j in range(1, n2 + 1):
                if text[i - 1] == pattern[j - 1] or pattern[j - 1] == '?':
                    curr[j] = prev[j - 1]
                elif pattern[j - 1] == '*':
                    curr[j] = prev[j] or curr[j - 1]
                else:
                    curr[j] = False

           
            prev, curr = curr, prev

        return prev[n2]