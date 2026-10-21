class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = 0
        for num in nums:
            total += num

        if total % 2 == 0:
            target = total // 2
            dp = [False] * (target + 1)
            dp[0] = True
            each_num_idx = 0
            while each_num_idx < len(nums):
                each_target = target
                while each_target >= nums[each_num_idx]:
                    dp[each_target] = dp[each_target] or dp[each_target - nums[each_num_idx]]
                    each_target -= 1
                each_num_idx += 1
            return dp[target]
        else:
            return False     
