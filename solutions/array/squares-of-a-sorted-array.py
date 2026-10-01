class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(result)-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                sq = nums[right] ** 2
                right -= 1
            else:
                sq = nums[left] ** 2
                left += 1
            
            result[i] = sq

        return result
