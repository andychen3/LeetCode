class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        
        res = 0
        prev_end = intervals[0][1]
        # print(intervals)
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
        return res
                