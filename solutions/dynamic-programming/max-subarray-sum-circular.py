class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        current_max = 0
        current_min = 0
        best_max = float('-inf')
        best_min = float('inf')
        total = 0
        for num in nums:
            total += num
        
        i = 0
        while i < len(nums):
            current_max = max(nums[i], current_max+nums[i])
            best_max = max(best_max, current_max)
            current_min = min(nums[i], current_min + nums[i])
            best_min = min(current_min, best_min)
            i += 1
        
        if total != best_min:
            max_cir_sum = total - best_min
            return max(max_cir_sum, best_max)
        else:
            return best_max
