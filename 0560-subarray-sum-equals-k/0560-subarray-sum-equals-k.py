class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        s = {0:1}

        for n in nums:
            cur+=n
            diff = cur-k

            res+= s.get(diff,0)

            s[cur] = 1+s.get(cur,0)
        return res