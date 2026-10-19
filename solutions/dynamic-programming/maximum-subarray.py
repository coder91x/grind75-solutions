class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # for i in range(1,len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])
        
        # return max(dp)
        
        if len(nums) == 1:
            return nums[0]

        current = 0
        best = float('-inf')

        for i in range(0, len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(best, current)
        
        return best
        
