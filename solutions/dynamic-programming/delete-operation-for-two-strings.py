class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]
        
        i = m - 1
        while i >= 0:
            j = len(dp[i]) - 2
            while j >= 0:
                if word1[i] == word2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    j -= 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    j -= 1
            i -= 1
        
        common_seq = dp[0][0]
        min_del = m + n - 2 * (common_seq)

        return min_del
        
