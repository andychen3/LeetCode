class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        prev = intervals[0][1]
        
        for interval in intervals[1:]:
            start, end = interval
            if start >= prev:
                prev = end
            else:
                ans += 1
                prev = min(prev, end)
        return ans