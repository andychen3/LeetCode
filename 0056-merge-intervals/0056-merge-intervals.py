class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        interval = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if interval[-1][1] < intervals[i][0]:
                interval.append(intervals[i])
            else:
                interval[-1][1] = max(interval[-1][1], intervals[i][1]) 
        return interval