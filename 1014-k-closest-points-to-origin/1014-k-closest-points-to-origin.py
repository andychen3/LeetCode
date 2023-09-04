import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(heap, (-distance, [x,y]))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [y for x, y in heap]