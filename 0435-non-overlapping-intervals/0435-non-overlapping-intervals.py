class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        ans = 0
        
        for interval in intervals[1:]:
            start, end = interval
            if start >= prev:
                prev = end
            else:
                ans += 1 
                prev = min(end, prev)
        return ans