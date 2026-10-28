class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tails = [envelopes[0][1]]
        i = 1
        while i < len(envelopes):
            if envelopes[i][1] > tails[-1]:
                tails.append(envelopes[i][1])
                i += 1
            else:
                left = 0
                right = len(tails) - 1
                while left < right:
                    mid = (left + right) // 2
                    if tails[mid] >= envelopes[i][1]:
                        right = mid
                    else:
                        left = mid + 1
                tails[left] = envelopes[i][1]
                i += 1
    
        lis = len(tails)
        return lis
