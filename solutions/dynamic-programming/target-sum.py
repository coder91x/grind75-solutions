class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = 0
        for num in nums:
            total += num
        
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0 
        sub_pos_target = (total + target) // 2

        i = 0
        dp = [0] * (sub_pos_target + 1)
        dp[0] = 1
        while i < len(nums):
            j = sub_pos_target
            while j >= nums[i]:
                dp[j] = dp[j] + dp[j - nums[i]]
                j -= 1
            i += 1
        
        return dp[sub_pos_target]
