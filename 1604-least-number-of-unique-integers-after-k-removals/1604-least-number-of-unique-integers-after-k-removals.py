from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        heap = []

        for key, freq in counts.items():
            heapq.heappush(heap, (freq, key))
        
        for _ in range(k):
            freq, key = heapq.heappop(heap)
            if freq - 1 != 0:
                heapq.heappush(heap, (freq-1, key))
        
        return len(heap)

