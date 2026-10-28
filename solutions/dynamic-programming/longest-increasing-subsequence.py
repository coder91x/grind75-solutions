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

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = [nums[0]]
        left = 0
        right = len(tails) - 1
        mid = (left + right) // 2
        i = 1
        while i < len(nums):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
                i += 1
            else:
                left = 0
                right = len(tails) - 1
                while left < right:
                    mid = (left + right) // 2
                    if tails[mid] >= nums[i]:
                        right = mid
                    else:
                        left = mid + 1
                tails[left] = nums[i]
                i += 1
        print(tails)
        lis = len(tails)
        return lis
