class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        seen = {0:1}
        count = 0
        curr_prefix = 0

        for i in range(len(nums)):
            curr_prefix += nums[i]
            prev_prefix = curr_prefix - k
            curr_rem = curr_prefix % k
            prev_rem = prev_prefix % k
            if prev_rem in seen:
                count += seen[prev_rem]
            seen[curr_rem] = seen.get(curr_rem, 0) + 1

        return count
