class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost) + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(len(cost) + 1):
            if i < len(cost):
                local_cost = cost[i]
            else:
                local_cost = 0
            dp[i] = min(local_cost + dp[i-1], local_cost + dp[i-2])
        return dp[-1]
