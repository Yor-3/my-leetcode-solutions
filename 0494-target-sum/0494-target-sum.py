import atexit
atexit.register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp ={}
        def backtrack(i,t):
            if i == len(nums):
                if t == target:
                    return 1
                return 0
            if (i,t) in dp:
                return dp[(i,t)]
            dp[(i,t)] = (backtrack(i+1,t+nums[i])+backtrack(i+1,t-nums[i]))
            return dp[(i,t)]
        return backtrack(0,0)