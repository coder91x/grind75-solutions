class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n+1)

        for i in range(len(ans)):
            ans[i] = ans[i // 2] + i % 2
        return ans
        # for i in range(len(ans)):
        #     num = i
        #     ones = 0
        #     while num != 0:
        #         if num % 2 == 1:
        #             ones += 1
        #         num = num // 2
        #     ans[i] = ones
        # return ans 
