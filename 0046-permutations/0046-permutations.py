class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums)==1:
            return [nums.copy()]

        for i in range(len(nums)):

            n = nums.pop(0)
            per = self.permute(nums)
            for p in per:
                p.append(n)
            res.extend(per)
            nums.append(n)

        return res
