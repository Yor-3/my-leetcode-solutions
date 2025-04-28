from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        cac = defaultdict(int)
        max_len = 0
        i = 0
        
        for j in range(len(s)):
            if cac[s[j]] != 0:
                i = max(i, cac[s[j]])
            max_len = max(max_len, j - i + 1)
            cac[s[j]] = j + 1

        return max_len
