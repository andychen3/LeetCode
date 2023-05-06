class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mergedIntervals = []
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if not mergedIntervals:
                mergedIntervals.append(interval)
            elif mergedIntervals[-1][1] >= interval[0]:
                mergedIntervals[-1] = [min(mergedIntervals[-1][0], interval[0]), max(mergedIntervals[-1][1], interval[1])] 
            else:
                mergedIntervals.append(interval)
        return mergedIntervals