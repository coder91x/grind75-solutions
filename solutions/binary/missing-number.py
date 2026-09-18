class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = len(nums)

        for x in range(len(nums)):
            result = result ^ x ^ nums[x]
        return result
