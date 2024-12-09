class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [-1 for i in range(len(cost)+1)]
        dp[0] = 0
        dp[1] = 0
        for floor in range(2, len(cost)+1):
            dp[floor] = min(cost[floor-1]+dp[floor-1], cost[floor-2]+dp[floor-2])
        return dp[-1]