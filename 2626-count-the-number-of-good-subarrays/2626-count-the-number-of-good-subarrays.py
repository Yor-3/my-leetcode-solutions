class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = r=0
        cnt = 0
        equal = 0
        res =0
        n = len(nums)
        freq=defaultdict(int)
        good =0

        while l<n:
            while r<n and equal<k:
                freq[nums[r]] +=1
                if freq[nums[r]]>=2:
                    equal +=(freq[nums[r]] -1)
                r+=1

            if equal>=k:
                good+=n-r+1

            freq[nums[l]]-=1
            if freq[nums[l]]>0:
                equal -=freq[nums[l]]
                
            l+=1

        return good
