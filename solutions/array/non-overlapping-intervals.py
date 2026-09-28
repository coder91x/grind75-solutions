class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda interval: interval[1])
        prev_end = intervals[0][1]
        removed = 0
        for interval in intervals[1:]:
            curr_start = interval[0]
            if prev_end > curr_start:
                removed += 1
            else:
                prev_end = interval[1]
        
        return removed
