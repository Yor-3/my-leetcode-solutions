class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
        mini =-1
        maxi=-1
        badi=-1
        ans= 0

        n = len(nums)

        for i in range(n):
            if nums[i] == mink:
                mini = i

            if nums[i] == maxk:
                maxi = i 

            if nums[i]< mink or nums[i]>maxk:
                badi = i

            ans += max(0,min(mini,maxi)-badi)

        return ans 