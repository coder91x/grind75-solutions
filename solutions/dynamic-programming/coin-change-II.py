class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        j = 0
        while j < len(coins):
            each_amount = 1
            while each_amount <= amount:
                if each_amount >= coins[j]:
                    dp[each_amount] = dp[each_amount] + dp[each_amount - coins[j]]
                each_amount += 1
            j += 1
        
        return dp[amount]
