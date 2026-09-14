class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] ==  nums[i-1]:
                continue
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                
                elif curr_sum > 0:
                    k -= 1 
                else:
                    j += 1
        return result
 

        



                    

        
