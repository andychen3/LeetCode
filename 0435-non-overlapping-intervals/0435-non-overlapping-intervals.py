class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        ans = 0
        end = intervals[0][1]
        
        for interval in intervals[1:]:
            if end > interval[0]:
                ans += 1
            else:
                end = max(end, interval[1])
        return ans