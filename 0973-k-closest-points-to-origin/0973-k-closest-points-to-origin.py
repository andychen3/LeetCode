import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x,y in points:
            distance = math.sqrt(((x-0)**2+(y-0)**2))
            heapq.heappush(heap, (-distance, [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point[1] for point in heap]
        