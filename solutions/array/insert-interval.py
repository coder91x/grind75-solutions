class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for currInt in intervals:
            if currInt[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = currInt
            elif currInt[1] < newInterval[0]:
                result.append(currInt)
            else:
                newInterval = [min(currInt[0], newInterval[0]), max(currInt[1], newInterval[1])]
        result.append(newInterval)
        return result
