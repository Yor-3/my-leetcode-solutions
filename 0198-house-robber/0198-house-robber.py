class Solution:

   


    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        


        prev1 =nums[0]
        prev2 =0
        
        for i in range(1,n):
            pick = nums[i]+prev2
            notpick = prev1

            cur = max(pick,notpick)
            prev2= prev1
            prev1 =cur

        return prev1

        