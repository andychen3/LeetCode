class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x : x[0])
        
        for index, interval in enumerate(intervals[1:]):
            if intervals[index][1] > interval[0]:
                return False
        return True