class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        i = 1
        while i < len(nums):
            j = 0
            while j < i:
                if nums[i] > nums[j]:
                    dp[i] = max(1 + dp[j], dp[i])
                    j += 1
                else:
                    j += 1
            i += 1
        
        return max(dp)
