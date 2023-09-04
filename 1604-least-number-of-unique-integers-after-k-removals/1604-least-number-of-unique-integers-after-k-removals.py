from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        heap = []

        # The reason this solution is slower because I am adding all n elements into the heap
        # Then i am iterating k times and performing log(n) operations.
        for key, freq in counts.items():
            heapq.heappush(heap, (freq, key))
        
        for _ in range(k):
            freq, key = heapq.heappop(heap)
            if freq - 1 != 0:
                heapq.heappush(heap, (freq-1, key))
        
        return len(heap)

