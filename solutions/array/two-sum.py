class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for x in range(len(nums)):
            compliment = target - nums[x]
            if compliment in hmap:
                return [hmap[compliment], x]
            hmap[nums[x]] = x
        return -1
