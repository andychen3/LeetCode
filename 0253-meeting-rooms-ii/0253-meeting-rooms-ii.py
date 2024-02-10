import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = []
        heappush(rooms, intervals[0][1])
        
        for interval in intervals[1:]:
            start, end = interval
            if rooms[0] <= start:
                heappop(rooms)
            heappush(rooms, end)
        return len(rooms)