class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(i, k, temp):
            # If the target is reached, add a copy of the current combination
            if k == 0:
                res.append(temp[:])
                return

            # If index goes out of bounds or target becomes negative, return
            if i >= len(c) or k < 0:
                return

            # Include the current element (stay at the same index)
            temp.append(c[i])
            helper(i, k - c[i], temp)
            temp.pop()  # Backtrack

            # Exclude the current element (move to the next index)
            helper(i + 1, k, temp)

        # Start backtracking
        helper(0, target, [])

        return res
