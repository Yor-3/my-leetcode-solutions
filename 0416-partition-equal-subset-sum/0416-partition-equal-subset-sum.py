class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1=sum(nums)
        if sum1&1: return False
        K=sum1//2
        dp=(1<<K)
        for x in nums:
            dp|=(dp>>x)
            if dp&1: return True
        return dp&1==1
        