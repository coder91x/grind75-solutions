class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        smallest_diff = abs(target - closest_sum)

        for i in range(len(nums)-1):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                diff = abs(target - curr_sum)

                if diff < smallest_diff:
                    smallest_diff = diff
                    closest_sum = curr_sum
                
                if curr_sum < target:
                    j += 1
                else:
                    k -= 1
                
        return closest_sum
