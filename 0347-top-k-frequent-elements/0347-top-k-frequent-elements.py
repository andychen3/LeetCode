from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [vals[1] for vals in heap]