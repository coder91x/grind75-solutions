class Solution:
    def rob(self, nums: list[int]) -> int:
        # dp[i] represnts max amount of money stolen onwards i
        next1 = 0
        next2 = 0
        i = len(nums) - 1
        result = 0
        while i >= 0:
            result = max(nums[i] + next2, next1)
            next2 = next1
            next1 = result
            i -= 1
        
        return result
