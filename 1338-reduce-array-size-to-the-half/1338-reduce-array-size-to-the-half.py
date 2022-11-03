import heapq
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hash_map = Counter(arr)
        length = len(arr)
        heap = []
        size = 0
        res = 0
        
        for key, val in hash_map.items():
            heapq.heappush(heap, (-val, key))
            
        while size < length/2:
            freq, key = heapq.heappop(heap)
            size -= freq
            
            res += 1
        
        return res
            
        