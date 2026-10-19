class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [0] * (len(cost) + 1)
        prev1 = 0
        prev2 = 0
        dp[0] = 0
        dp[1] = 0

        i = 2
        while i <= len(cost):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            i += 1
        
        return dp[-1]

        n = len(cost)
        prev1 = 0
        prev2 = 0
        result = 0

        for i in range(2, n + 1):
            result = min(cost[i-1] + prev1, cost[i-2] + prev2)
            prev2 = prev1
            prev1 = result
        
        return result
