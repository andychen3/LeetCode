import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-x for x in piles]
        
        heapq.heapify(max_heap)
        
        while k > 0:
            k -= 1
            largest_pile = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (largest_pile//2))
            
        return abs(sum(max_heap))
        
        