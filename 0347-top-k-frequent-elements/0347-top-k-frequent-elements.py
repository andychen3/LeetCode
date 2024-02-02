from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        
        for key, val in counts.items():
            heappush(heap, (val, key))
            while len(heap) > k:
                heappop(heap)            
        
        return [key for val, key in heap]