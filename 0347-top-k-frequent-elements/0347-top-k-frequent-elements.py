import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        arr = []
        
        for key, val in counts.items():
            heappush(heap, (-val, key))
        
        for _ in range(k):
            freq, key = heappop(heap)
            arr.append(key)
        return arr