import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        
        for x, y in points:
            euclidean = math.sqrt((x - 0)**2 + (y - 0) ** 2)
            heappush(heap, (-euclidean, [x, y]))
            while len(heap) > k:
                heappop(heap)
        return [val[1] for val in heap]