class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        seen = {0:1}
        count = 0
        curr_prefix = 0

        for i in range(len(nums)):
            curr_prefix += nums[i]
            prev_prefix = curr_prefix - goal
            if prev_prefix in seen:
                count += seen[prev_prefix]
            seen[curr_prefix] = seen.get(curr_prefix, 0) + 1

        return count
