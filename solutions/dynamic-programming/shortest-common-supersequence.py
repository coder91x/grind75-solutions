class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        s1 = str1
        s2 = str2
        result = []

        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        i = m - 1
        while i >= 0:
            j = n - 1
            while j >= 0:
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    j -= 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    j -= 1
            i -= 1
        
        i = 0
        j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                result.append(s1[i])
                i += 1
                j += 1
            elif dp[i][j+1] >= dp[i+1][j]:
                result.append(s2[j])
                j += 1
            else:
                result.append(s1[i])
                i += 1
        
        result.extend(s1[i:])
        result.extend(s2[j:])

        return "".join(result)
