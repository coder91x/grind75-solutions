class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}

        # def help(n):
        #     if n == 1: return 1
        #     if n == 2: return 2

        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = help(n-2) + help(n-1)
            
        #     return memo[n]
        
        # return help(n)

        if n == 1 : return 1
        if n == 2 : return 2
        prev1 = 2
        prev2 = 1
        result = 0

        i = 3
        while i <= n:
            result = prev1 + prev2
            prev2 = prev1
            prev1 = result
            i += 1
        
        return result
       
