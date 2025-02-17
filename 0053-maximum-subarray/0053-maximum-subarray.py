class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        cursum = 0
        maxsum=n[0]

        for i in range(len(n)):
            if cursum<0:
                cursum=0
            cursum+=n[i]
            maxsum = max(maxsum,cursum)
        return maxsum