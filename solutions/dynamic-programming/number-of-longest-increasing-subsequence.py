class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)
        i = 1
        while i < len(nums):
            j = 0
            while j < i:
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == 1 + dp[j]:
                        count[i] = count[j] + count[i]
                j += 1
            i += 1
        lis = max(dp)
        answer = 0
        for i in range(len(nums)):
            if dp[i] == lis:
                answer = answer + count[i]
            
        return answer
