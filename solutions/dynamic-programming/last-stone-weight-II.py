import math
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total_weight = 0
        for stone_weight in stones:
            total_weight += stone_weight

        target_weight = math.floor(total_weight // 2)
        print(target_weight)

        if target_weight > total_weight: return 0
        dp = [False] * (target_weight + 1)
        dp[0] = True
        i = 0
        while i < len(stones):
            j = target_weight
            while j >= stones[i]:
                dp[j] = dp[j] or dp[j - stones[i]]
                j -= 1
            i += 1
        
        j = target_weight
        while j >= 0:
            if dp[j]:
                largest_idx = j
                break
            j -= 1
        
        smallest_weight = total_weight - 2 * (largest_idx)

        return smallest_weight
