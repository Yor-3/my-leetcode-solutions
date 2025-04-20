class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key =len)
        def compare(a, b):
            if len(a) + 1 != len(b):
                return False

            i = j = 0
            while j < len(b):
                if i < len(a) and a[i] == b[j]:
                    i += 1
                j += 1

            return i == len(a)

        n = len(words)
        dp = [1 for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if compare(words[i],words[j]) and dp[i]<(1+dp[j]):
                    dp[i] = 1+dp[j]

        return max(dp)
        