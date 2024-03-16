import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]
        
        for interval in intervals[1:]:
            start, end = interval
            
            if start >= heap[0]:
                heappop(heap)
            heappush(heap, end)
        return len(heap)