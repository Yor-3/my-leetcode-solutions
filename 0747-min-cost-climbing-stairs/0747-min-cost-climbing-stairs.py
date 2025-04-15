class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # Base cases
        prev2 = cost[0]
        prev1 = cost[1]

        # Iterate through the stairs from the 2nd step to the last step
        for i in range(2, n):
            cur = min(prev1, prev2) + cost[i]
            prev2 = prev1  # Move prev1 to prev2
            prev1 = cur    # Update prev1 to the current cost

        # The minimum cost to reach the top (after the last step)
        return min(prev1, prev2)
