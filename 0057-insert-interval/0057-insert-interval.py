class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = []
        end = []
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                start.append(interval)
            elif interval[0] > newInterval[1]:
                end.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        return start + [newInterval] + end