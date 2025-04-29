class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        large = max(nums)
        number = 0
        l =0
        res=0
        for r in range(len(nums)):
            if nums[r] == large:
                number+=1

            while number>=k:
                if nums[l] == large:
                    number-=1

                l+=1

            res+=l

        return res

        
