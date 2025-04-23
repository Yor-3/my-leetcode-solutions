class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = [0] * 37  
        for i in range(1, n + 1):
            s = 0
            x = i
            while x:
                s += x % 10
                x //= 10
            count[s] += 1

        max_val = max(count)
        return count.count(max_val)
