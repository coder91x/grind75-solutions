class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []
        i = 0
        while i < len(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                popped = stack.pop()
                answer[popped[1]] = i - popped[1]
            stack.append((temperatures[i], i))
            i += 1
        
        return answer
