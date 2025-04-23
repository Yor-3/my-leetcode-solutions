class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import Counter
        c = Counter(sum(map(int, str(i))) for i in range(1, n+1))
        return list(c.values()).count(max(c.values()))
