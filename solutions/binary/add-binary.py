class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        digits = []

        while i >= 0 or j >= 0:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry
            digit = total % 2
            carry = total // 2

            digits.append(str(digit))
            i-= 1
            j-= 1

        if carry > 0:
            digits.append(str(carry))

        return "".join(reversed(digits))
