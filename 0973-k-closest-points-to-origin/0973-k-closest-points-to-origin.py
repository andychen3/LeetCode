import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            euc_distance = -sqrt((point[0]-0)**2+(point[1]-0)**2)
            heapq.heappush(heap, (euc_distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [key[1] for key in heap]
            