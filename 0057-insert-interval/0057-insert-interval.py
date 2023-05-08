class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for index, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[index:]
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        res.append(newInterval)
        return res
            
        
        