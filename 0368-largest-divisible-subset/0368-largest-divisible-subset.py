class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n= len(nums)
        dp  = [1 for _ in range(n)]
        prev = [-1 for _ in range(n)]
        for i in range(n-1,-1,-1):  
            for j in range(i+1,n):
                if nums[j]%nums[i]==0 and dp[i]<(1+dp[j]):
                    dp[i] =1+dp[j]
                    prev[i] = j

            
        max_ind = dp.index(max(dp))

        seq = []
        while max_ind !=-1:
            seq.append(nums[max_ind])
            max_ind = prev[max_ind]


        

        return seq