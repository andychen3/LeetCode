import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            second = heapq.heappop(max_heap)
            first = heapq.heappop(max_heap)
            
            if first != second:
                heapq.heappush(max_heap, -first+second)
        
        return abs(max_heap[0]) if len(max_heap) == 1 else 0