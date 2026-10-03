class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        min_len = float('inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                window_len = i - left + 1
                min_len = min(min_len, window_len)
                curr_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0
        
