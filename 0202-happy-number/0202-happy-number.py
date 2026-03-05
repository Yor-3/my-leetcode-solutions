class Solution:
    
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n

        while True:
            slow = self.sumSquareDigits(slow)
            fast = self.sumSquareDigits(self.sumSquareDigits(fast))

            if slow == fast:
                break

        return slow == 1

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
