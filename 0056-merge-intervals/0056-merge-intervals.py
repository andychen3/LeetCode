class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]
        
        for interval in intervals[1:]:
            prev_end = res[-1][1]
            start = interval[0]
            end = interval[1]
            
            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            else:
                res.append(interval)
        return res
        
        
        