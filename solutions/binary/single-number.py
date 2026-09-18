class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # hmap = {}
        # for x in nums:
        #     if x in hmap:
        #         hmap[x] += 1
        #     else:
        #         hmap[x] = 1
        
        # for x in hmap:
        #     if hmap[x] == 1:
        #         return x
        
        result = 0
        for num in nums:
            result = result ^ num
        return result
