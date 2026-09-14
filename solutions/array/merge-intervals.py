class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for curr in intervals:
            last_merged = result[-1]
            if curr[0] <= last_merged[1]:
                last_merged[1] = max(curr[1], last_merged[1])
            else:
                result.append(curr)
        return result

       
