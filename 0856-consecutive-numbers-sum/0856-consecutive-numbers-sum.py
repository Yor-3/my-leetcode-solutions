class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n == 1:
            return 1
        
        ans: int = 0
        if n % 2:
            ans = 2
        else:
            ans = 1
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                if (n // i) % 2:
                    ans += 1
                if (i % 2) and i != n**0.5:
                    ans += 1
        
        return ans
        