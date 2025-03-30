from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue  # Skip duplicates for `a`

            l, r = i + 1, len(nums) - 1  # ← Correctly define `l` and `r` here

            while l < r:
                s = a + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])  # ← Use list brackets `[]`

                    # Skip duplicates for `l` and `r`
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # Move both pointers after finding a valid triplet
                    l += 1
                    r -= 1

        return res
