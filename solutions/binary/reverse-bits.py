class Solution:
    def reverseBits(self, n: int) -> int:
        # result = 0
        # for i in range(32):
        #     result = result * 2 + n % 2
        #     n = n // 2
        # return result

        digit = [0] * 32

        i = len(digit) - 1
        while n != 0:
            digit[i] = n % 2
            i -= 1
            n = n // 2
        
        digit.reverse()
        result = 0

        for i in range(len(digit)):
            power = len(digit) - i - 1
            result += digit[i] * (2 ** power) 
        
        return result
        

             
