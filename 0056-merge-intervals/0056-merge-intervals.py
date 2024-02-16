class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        interval = [intervals[0]]
        
        for i in intervals[1:]:
            if interval[-1][1] >= i[0]:
                interval[-1][1] = max(interval[-1][1], i[1])
            else:
                interval.append(i)
        return interval