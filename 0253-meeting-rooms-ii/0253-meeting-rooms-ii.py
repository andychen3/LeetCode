import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]
        
        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            
            if start >= heap[0]:
                heappop(heap)
            
            heappush(heap, end)
        return len(heap)