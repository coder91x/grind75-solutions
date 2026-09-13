class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hmap and hmap[compliment] != i:
                return i, hmap[compliment]
            hmap[nums[i]] = i
        return -1
