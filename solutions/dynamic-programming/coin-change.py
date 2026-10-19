class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) 
        dp[0] = 0
        each_amount = 1
        while each_amount <= amount:
            denomination = 0
            while denomination < len(coins):
                if coins[denomination] > each_amount:
                    denomination += 1
                else:
                    dp[each_amount] = min(dp[each_amount], dp[each_amount - coins[denomination]] + 1)
                    denomination += 1     
            each_amount += 1
        
        return dp[amount] if dp[amount] != float('inf') else -1
        
