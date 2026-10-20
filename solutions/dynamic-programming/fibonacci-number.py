class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n ==1 : return 1
        prev2 = 0 
        prev1 = 1
        result = 0 

        for i in range(2,n+1):
            result = prev2 + prev1
            prev2 = prev1
            prev1 = result

        return result

        memo = {}

        def help(n):
            if n == 0: return 0
            if n == 1: return 1

            if n in memo:
                return memo[n]
            else:
                memo[n] = help(n-1) + help(n-2)
            
            return memo[n]
        
        return help(n)


        if n == 0: return 0
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        i = 2
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1

        
        return dp[n]


