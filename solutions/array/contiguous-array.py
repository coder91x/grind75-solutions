class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if i == 0 else i for i in nums]
        balance = 0
        seen = {0:-1}
        max_length = 0

        for i, num in enumerate(nums):
            balance += num
            if balance in seen:
                max_length = max(max_length, i - seen[balance])
            else:
                seen[balance] = i
        
        return max_length
