class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        next2a = 0
        next1a = 0
        next2b = 0
        next1b = 0
        r1 = 0
        r2 = 0
        i = n - 2
        j = n - 1
        while i >= 0:
            r1 = max(nums[i] + next2a, next1a)
            next2a = next1a
            next1a = r1
            i -= 1
        
        while j >= 1:
            r2 = max(nums[j] + next2b, next1b)
            next2b = next1b
            next1b = r2
            j -= 1

        return max(r1, r2)


        
        
        

        
        
