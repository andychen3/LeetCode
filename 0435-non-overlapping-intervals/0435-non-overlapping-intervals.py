class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        ans = 0
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= prev:
                prev = end
            else:
                ans += 1
                prev = min(prev, end)
        return ans