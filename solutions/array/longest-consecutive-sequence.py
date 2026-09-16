class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        i = 0
        # for i in range(len(nums)):
        while i < len(nums):
            length = 1
            if nums[i] - 1 in num_set:
                i += 1
                # continue
            else:
                curr_num = nums[i]
                while curr_num + 1 in num_set:
                    length += 1
                    curr_num += 1
                max_length = max(length, max_length)
                i += 1
        return max_length
