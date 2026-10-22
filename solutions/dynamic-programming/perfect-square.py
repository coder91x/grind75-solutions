class Solution:
    def numSquares(self, n: int) -> int:
        square = []
        k = 1
        while (k ** 2) <= n:
            square.append(k**2)
            k += 1
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        i = 0
        while i < len(square):
            j = 1
            while j <= n:
                if j >= square[i]:
                    dp[j] = min(dp[j], dp[j - square[i]] + 1)
                    j += 1
                else:
                    j += 1
            i += 1
        
        return dp[n]
