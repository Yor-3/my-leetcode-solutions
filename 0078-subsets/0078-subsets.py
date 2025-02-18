class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        sub = []

        def create(i):
            if i == len(nums):
                res.append(sub[:])
                return

            sub.append(nums[i])
            create(i+1)
            sub.pop()
            create(i+1)

        create(0)
        return res