class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i = 0
        window_sum = 0
        while i < k:
            window_sum += nums[i]
            i += 1
        
        best_sum = window_sum

        j = k
        while j < len(nums):
            incoming = nums[j]
            outgoing = nums[j - k]
            new_sum = window_sum + incoming - outgoing
            window_sum = new_sum
            best_sum = max(best_sum, new_sum)
            j += 1
        
        return best_sum / k

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        
        best_sum = window_sum

        for j in range(k, len(nums)):
            incoming = nums[j]
            outgoing = nums[j-k]
            new_sum = window_sum - outgoing + incoming
            best_sum = max(best_sum, new_sum)
            window_sum = new_sum
        
        return best_sum / k


     

        
